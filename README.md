# HiQA
Paper: [HiQA: A Hierarchical Contextual Augmentation RAG for Massive Documents QA, arXiv:2402.01767](https://arxiv.org/abs/2402.01767)


HiQA offers a suite of tools designed for document processing, which includes segmenting documents into sections, enhancing them with metadata, and embedding them for detailed analysis. 
This is followed by employing a multi-route retrieval system to search for relevant knowledge in response to a specific question. 
The identified knowledge, alongside the question, is then fed into a large language model (LLM) to generate an answer. 
While processing documents might incur some costs, this one-time process substantially enhances the quality of the outcomes.  

# How to use
1. Python version == 3.9
2. pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
3. Set your own OpenAI key
4. Start demo: PYTHONUNBUFFERED=1 nohup streamlit run app_streamlit.py --server.port 8080 --server.address 0.0.0.0 > logs/run.log 2>&1 &
5. The above command requires manually make a directory 'logs' 

# How to create your own dataset?
1. Files in 'build_tool' contains all tools for building a dataset.
2. For a given pdf file (note that the pdf should be able to extract text)
3. Step1, using pdf2md to convert pdf file into a well-formatted markdown, this step use gpt-4-turbo-preview (0125).
4. Step2, using md2csv to convert markdown into a csv file contains splitting sections. Sections now contains hierarchy meta-data and tables are labeled.
5. Step3, using section2embedding to add embedding vector.
6. Step4, put all processed csv files into a dataset directory, load this in knowledge_client.py, and allow to query in app_streamlit.py demo.
Notice that we passing all file name and file title to Named Entity Detect models to generate critic keywords, and storing in utils.filter.critic_keywords. 

# How to extract and search images from a pdf?
In image_service, load, build, and commit, this will create a directory /indexes of whoosh.
One can use vlm (like ollama -> llava:34b) to generate description of each extracted image.
Image search refer to app_streamlit.search_images_from_response
