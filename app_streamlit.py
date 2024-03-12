import streamlit as st
from utils.tokenizer import ChineseTokenizer
from service.knowledge_client import *
from utils.openai_proxy import client
from dotenv import load_dotenv

load_dotenv()

# ------------ Streamlit App ------------
# init page
st.set_page_config(page_title="HiQA System")

st.header("HiQA System")

if __name__ == '__main__':

    gpt_version = '1'

    dataset = st.selectbox('Select a dataset',
                           ['Product documents - Texas Instruments', 'Product documents - Chipanalog',
                            'Book - Analog integrated circuit design', 'Annual financial reports'])
                            # 'Ablation - Origin TI', 'Ablation - without HCA TI', 'Ablation - fix chunk TI'])
    max_tokens = st.selectbox('knowledge length', ['short', 'long'])
    if max_tokens == 'short':
        max_tokens = 2000
    else:
        max_tokens = 8000

    vec_only = st.selectbox('vec_only', ['False', 'True'])
    if vec_only == 'True':
        only_vec = True
    else:
        only_vec = False

    user_input = st.text_input("Enter your query: ")
    show_images = st.checkbox('Use Image', key="unique_key_for_show_images")

    role = """Role: You are a helpful assistant, you will answer questions as a professional support agent.\n" Note:
1. When users ask questions, I will provide you with some information, please refer to the information and your own knowledge to answer.
2. Each data Paragraph begins with "*** New Knowledge Paragraph ***", the next line [Source File] xxx [Source File] indicates the source of the file, The next line [Knowledge Title] xxx [Knowledge Title] indicates the title of this section, and the next line [Knowledge Content] xxx [Knowledge Content] is the knowledge content you are referring to.
3. Your answers should be accurate and reasonable, but not summary.
4. If your own knowledge and given information cannot answer the user's question, do not answer and tell the user "Sorry, I cannot answer your question."
5. There are redundant parts in the reference materials provided by us. Please ignore the materials that are not relevant to the question.
6. If you are asked to answer a multiple choice question (single choice or multiple choice), analyze each choice first. After analyzing the choices, write the answer.
7. If you use the table in your answer, please output the table in markdown's table format. The format of the table must strictly use markdown's format.
8. If some data is not directly given, try to calculate through the given data first, show the calculation process, and then answer the question after the calculation step is complete.
9. Please focus on answering the user's question, do not answer with irrelevant information."""

    if st.button('Submit'):
        # set gpt version
        if gpt_version == '2':
            model_name = "gpt-3.5-turbo-1106"
        elif gpt_version == '1':
            model_name = 'gpt-4-1106-preview'

        query = user_input
        st.session_state.selected_faq = None
        st.markdown("----")
        res_box = st.empty()
        image_placeholder = st.empty()
        print('begin...')
        user_input = query
        if user_input:
            begin = time.time()
            # response = get_response_from_openai(user_input, begin)
            response = ''
            knowledge = get_knowledge(user_input, max_tokens, dataset, begin, only_vec=only_vec, verbose=True)
            print('\nknowledge:\n' + knowledge + '\n\n')

            if gpt_version == "1" or gpt_version == "2":
                report = []
                # Looping over the response
                for resp in client.chat.completions.create(
                        model=model_name,
                        # model='gpt-4-32k',
                        # max_tokens=4000,
                        messages=[
                            {"role": "system",
                             "content": role},
                            {"role": "user",
                             "content": f"According to the given knowledge, answer this question: {user_input}\nThe given knowledge is: \n{knowledge}"}
                        ],
                        stream=True
                ):
                    try:
                        report.append(resp.choices[0].delta.content)
                        result = "".join(report).strip()
                        res_box.markdown(f'*{result}*')

                        res_box.write(result)
                    except:
                        pass
                report = [s for s in report if s is not None and s != '']
                response = "".join(report).strip()

            st.markdown("----")
            print('after gpt, ' + str(time.time() - begin))
            if show_images and (dataset == 'Product documents - Chipanalog' or
                                dataset == 'Book - Analog integrated circuit design' or
                                dataset == 'Product documents - Texas Instruments'):
                # images = search_images_from_response(response)
                try:
                    images = search_images_from_response(user_input, response, dataset)
                    print('after img, ' + str(time.time() - begin))
                    for img, title, score, file_name, content in images[:1]:
                        file_name = '_'.join(file_name.split('_')[:-3])
                        if title != 'Title not found':
                            image_placeholder.image(img, caption="Source - " + file_name + ",\t" + title)
                        else:
                            image_placeholder.image(img, caption="Source - " + file_name)
                except Exception as e:
                    pass
