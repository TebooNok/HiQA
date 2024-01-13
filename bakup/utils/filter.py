def contains_str(input_str, keyword):
    return keyword in input_str
def filter_product_names(user_query, product_list):
    filter_name = []
    for product in product_list:
        if product in user_query:
            filter_name.append(product)

    if not filter_name:
        pass
    return filter_name



def rank_values(multi_product):
    ranked_list = []

    # Extract the 'multi' and 'no_product' keys and values
    multi_values = multi_product.get('multi', []).copy()
    no_product_values = multi_product.get('no_product', []).copy()
    un_keyword_values = multi_product.get('un_keyword', []).copy()

    # Get the other keys
    other_keys = [key for key in multi_product.keys() if key not in ['multi', 'no_product', 'un_keyword']]

    # While there are still values in 'multi' and any of the other keys
    while multi_values or any(multi_product[key] for key in other_keys):
        if multi_values:
            ranked_list.append(multi_values.pop(0))
        for key in other_keys:
            if multi_product[key]:
                ranked_list.append(multi_product[key].pop(0))

    # Finally, add the 'no_product' values
    ranked_list.extend(no_product_values)
    ranked_list.extend(un_keyword_values)
    return ranked_list

def filter_knowledge(question, results, default_keyword, default_unkeyword):
    # openai.api_key = open_ai_api_key
    query_list = filter_product_names(question, default_keyword)

    multi_product = {}
    multi_product["multi"] = []
    multi_product["no_product"] = []
    multi_product['un_keyword'] = []
    for i in query_list:
        multi_product[i] = []

    # print("Step 1")
    all_text = ''
    if len(query_list) == 0:
        for text in results['documents'][0]:
            all_text += text.replace('[desc]', '') + '\n'
        return [all_text]
    else:

        for text in results['documents'][0]:
            content_list = filter_product_names(text, query_list)
            un_content_list=filter_product_names(text, default_unkeyword)
            if len(un_content_list)!=0:
                multi_product["un_keyword"].append(text.replace('[desc]', ''))
                continue
            if len(content_list) == 0:
                multi_product["no_product"].append(text.replace('[desc]', ''))
            elif len(content_list) > 1:
                multi_product["multi"].append(text.replace('[desc]', ''))
            else:
                # print("content is" + content_list[0])
                multi_product[content_list[0]].append(text.replace('[desc]', ''))
    # print("Step 2")
    rank_list = rank_values(multi_product)

    return rank_list


