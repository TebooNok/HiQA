# Define a function to filter product names from a user's query
import re
import os
import re
import csv

###
critic_keywords = list(
    {'川土微', '共模电压', '超宽体', '增强型数字隔离器', 'IS373', 'CA-IS3105w', 'CA-IS3740lw', 'CA-IF1042vs-q1',
     'IS3722HS', 'IS3541', 'CA-IF4850HS', 'CAIS3730LW', 'CA-IS3642lw', 'IS362', 'IS3740HB', 'CA-IS3761lw', 'IS3531',
     'IS1306M25G', 'IS3760LN', 'CA-IS3643HW', 'CA-IS3730HW', 'CA-IS3101B', 'CA-IF1021s-q1', 'CA-IS3721lw',
     'CA-IS3762HW', 'CA-IF1042S Q1', 'CA-IS3731HB', 'CA-IS3720hs', 'IF4888', 'CA-IS3742hw', 'IS3760HN', 'CA-IF4820hs',
     'CA-IS3740hw', 'CS48520M', 'CA-IS3102W', 'CAIS3760HW', 'IS2631', 'CA-IS3740hb', 'IS3643LW', 'CA-IS3092w',
     'CAIS3760LW', 'CA-IS3741HN', 'CAIF4820HD', 'CA-IS3720hw', 'CAIS3722HW', 'IS3102', 'IS308', 'CA-IS3104W',
     'CA-IS3760HN', 'CA-IS3762hw', 'CAIS3722HS', 'CA-IS3760HW', 'CA-IS3760ln', 'CA-IS3643hw', 'CA-IS3730HB',
     'CA-IS3721LS', 'CAIS3640HW', 'CAIS3105W', 'IS3721LS', 'IS3720', 'CA-IS3761hw', 'IS2082B', 'CA-IS1306m25g',
     'CA-IS3980P', 'CA-IS3021S', 'CA-IS3980p', 'IS3641LW', 'CAIS3730LN', 'CA-IS3763hn', 'CA-IF1051HS', 'IS3642LW',
     'CA-IS3742LW', 'cs48505d', 'CA-IF1051S Q1', 'CAIS3104W', 'IS3761LW', 'CA-IS3740HN', 'CA-IF1051hs', 'IS3050G',
     'CA-IS3763ln', 'CA-IS3104w', 'CA-IS3082WNX', 'CA-IS3640LW', 'CA-IS3720LW', 'IS3742HB', 'IS3710', 'CA-IS3722HW',
     'Q100', 'CA-IS3722LS', 'CAIF1042VSQ1', 'CA-IS3050W', 'CA-IS3721LW', 'CA-IF1044s-q1', 'CAIS3740HN', 'CA-IF4820HM',
     'IS3730LW', 'CA-IF1044S Q1', 'CA-IS3730LW', 'CA-IS3730ln', 'CAIS3731HW', 'CA-IS3741HN', 'CAIS3731LN', 'CAIS3722LS',
     'CAIS3052G', 'IS3721HS', 'CAIS3050W', 'CA-IS3721HW', 'CA-IS3730HB', 'CA-IS3104W', 'IS1300G25G', 'CA-IS3644lw',
     'CA-IS3761LN', 'CA-IS3730lw', 'CA-IS3761HW', 'CA-IS3640HW', 'CAIS3988P', 'CA-IS3721LS', 'CA-IF4850HS',
     'CA-IS3086wx', 'IS3062', 'IS305', 'CA-IF4820fs', 'IS3740', 'CA-IS3050U', 'CA-IF4023', 'CAIS3742HB', 'CA-IS3730LN',
     'CA-IS3020S', 'IS374', 'CAIF4850HS', 'CA-IS1200U', 'CA-IS3640lw', 'IS3080WX', 'CA-IS3731hw', 'CA-IS3720HG',
     'CA-IS3762hn', 'CA-IS3740ln', 'IS3731HB', 'CA-IS3720hg', 'CAIS3644LW', 'CAIF4820FS', 'CA-IS3721HW', 'IS3740LW',
     'CAIS3763LN', 'CA-IS3761LN', 'CA-IS3742LN', 'CA-IS3052G', 'CA-IS3763HW', 'CAIS3731HB', 'CA-IS3762LW', 'IS3082WX',
     'CA-IS3741LW', 'CA-IS3763HN', 'IS3741LN', 'CA-IS3760hw', 'IS3731HN', 'CA-IS3720HS', 'CAIS3731LW', 'CAIS3642LW',
     'IS3722HG', 'CA-IF1042VS-Q1', 'CAIS3761LN', 'CA-IF4888HS', 'CA-IS3080WX', 'CA-IS3740LW', 'IS3640LW', 'CA-IS3020W',
     'CA-IS3640LW', 'CA-IS3741HW', 'CAIS3722HG', 'CA-IS3722LG', 'IS3730LN', 'CA-IS3642LW', 'CAIS1200G', 'CA-IS3641HW',
     'CA-IS3050W', 'CAIS3760HN', 'IS3740LN', 'CAIS2082B', 'IF4420', 'CS48520D', 'IS3741HW', 'CAIS1306M25G',
     'CA-IS3082wnx', 'CA-IS3720LG', 'cs48520d', 'IF1042', 'CA-IS3761LW', 'CAIS3643HW', 'CAIS3740HW', 'CA-IS3988P',
     'CA-IS3763hw', 'IS3105W', 'CAIS3742LW', 'CA-IS3761HW', 'CA-IF1021S-Q1', 'CAIS3721LS', 'CA-IS3763LN', 'CA-IS3740HW',
     'CA-IS3720ls', 'CA-IS3080WX', 'IS3762HW', 'CA-IS3722LW', 'CA-IS3760LN', 'CA-IF4888HS', 'CA-IS3742lw', 'IF1044',
     'CA-IS3731HN', 'IS2092', 'CA-IS3730LW', 'IS3092_3098', 'CA-IS3642LW', 'CA-IS3730HW', 'CA-IS3721hs', 'IS3722LW',
     'CA-IS3730HN', 'CA-IS3644HW', 'CA-IS3021S', 'CAIF1051SQ1', 'CA-IS3020S', 'CAIF1051HS', 'CA-IS3763LW',
     'CA-IS1300G25G', 'IS372', 'CA-IS3763lw', 'IS1305AM25W', 'IF4805HS', 'CA-IS3644HW', 'CA-IS3980s', 'CA-IS3742HB',
     'IS3115', 'CAIS3741HW', 'CAIS3720HG', 'CA-IS3082wx', 'CA-IS3760lw', 'CA-IS3760HW', 'CAIS1204W', 'CA-IF4820FS',
     'IS3082WNX', 'CA-IS3722hs', 'CA-IS3722HG', 'CA-IF4820FS', 'CA-IS3762HN', 'IS2082', 'IS3722HW', 'cs48520m',
     'CS48505M', 'CA-IS3720LS', 'CA-IS3760HN', 'CA-IS3021W', 'CA-IS1200g', 'CS817x20LS', 'IS3740HW', 'CAIS3641HW',
     'IS322', 'CA-IS3720LG', 'IS3088WX', 'IS3221_2', 'CA-IS3731ln', 'CA-IS3763HN', 'CA-IS3730HN', 'CA-IS3722lw',
     'CAIS3741LW', 'IF4820HD', 'CA-IS3742HW', 'CA-IS3760LW', 'CA-IF1042s-q1', 'CAIS3082WX', 'CA-IS1306M25G',
     'CA-IS3762ln', 'CA-IS3731LW', 'CA-IS3741hw', 'CA-IF4850hs', 'CA-IS3740HW', 'CA-IS3082WX', 'CA-IS3721HS',
     'CAIS3722LW', 'CAIS3720HW', 'CAIS3720LG', 'CA-IF4805HS', 'IS3742LN', 'CA-IS3050U', 'CA-IS3763LN', 'IS3730HW',
     'CAIS3642HW', 'CA-IS3731LW', 'IS2062', 'CA-IS3741LB', 'CA-IS3988p', 'CA-IS3760hn', 'IF1051HS', 'CA-IS3742HB',
     'CAIS3740LN', 'CAIS3086WX', 'CA-IS3740LN', 'IS3052G', 'CAIF4023', 'CAIS3742HW', 'CA-IF4820hd', 'CAIS3088WX',
     'CA-IS3762HW', 'CA-IS3731lw', 'CA-IS3642HW', 'IS3762LN', 'IF4023', 'CA-IS3980S', 'IS1200U', 'CAIS3721LW',
     'CA-IF4820HS', 'IS376', 'CAIS3640LW', 'CAIS3102W', 'CA-IS3741HW', 'CA-IF1044VS-Q1', 'CA-IS1204W', 'IS3761HN',
     'IS3763LW', 'CA-IS3050u', 'CA-IS3731HN', 'CA-IS3644LW', 'IS382', 'CA-IS3050G', 'CAIF4805HS', 'CA-IS3092W',
     'CA-IS3762LN', 'CA-IS3721LW', 'CA-IS3740LN', 'IS3020S', 'IS3720HS', 'IS3020W', 'CA-IS3741ln', 'IF4820HS',
     'CAIS3742LN', 'CS48520S', 'IF4220', 'CA-IS3050g', 'IS3092W_98', 'CAIS3021W', 'IS1311', 'IF1028', 'IF1021S-Q1',
     'CA-IF4805hs', 'IS3104W', 'CA-IS3761ln', 'IS3740HN', 'CAIF1044VSQ1', 'CA-IS3105W', 'CA-IF1042VS Q1', 'CS485',
     'CA-IS2082B', 'CA-IS3720LS', 'IF1044VS-Q1', 'IS3762HN', 'IS1300', 'IS1044', 'CAIS3021S', 'CA-IS3742hb',
     'CA-IS3643HW', 'CA-IS3720HG', 'CAIS3644HW', 'CA-IS3720lg', 'CAIS3643LW', 'IF1044S-Q1', 'CA-IS3762HN', 'IS3761HW',
     'CA-IS3088WX', 'CA-IS3763HW', 'CA-IS3722lg', 'CA-IS3742HW', 'CA-IS1300g25g', 'IS3092W', 'IS364', 'IS3102W',
     'IS3720LW', 'CA-IS3088WX', 'CAIS3762LN', 'CA-IF4023', 'IS3731LW', 'CAIS3050U', 'CA-IS3730hn', 'CA-IS3643LW',
     'CAIS3980S', 'CA-IS3020W', 'IS1044S', 'CA-IF4820HM', 'CA-IS3644hw', 'CA-IS3741LN', 'CA-IS3722HS', 'CA-IS3722HS',
     'CA-IS3640HW', 'CA-IS3102W', 'IS3731HW', 'IS3722LS', 'CA-IS3101B', 'CA-IS1300G25G', 'CA-IS3742LW', 'CA-IS3644LW',
     'IS3722LG', 'CA-IS3742HN', 'IS3211', 'CA-IS1305AM25W', 'IS3741LB', 'IS3731LN', 'IS3762LW', 'CA-IS1204W',
     'CAIS3052W', 'CA-IS3740LW', 'IS3720LS', 'CA-IS3760LN', 'CA-IS1305AM25W', 'CA-IS3050G', 'CA-IS3088wx', 'CAIS3980P',
     'CAIS3760LN', 'CAIF1051VSQ1', 'cs48505s', 'CAIS3741HN', 'CAIS3730HW', 'IS3763HW', 'CA-IS1200G', 'CA-IS3082WNX',
     'IS3050W', 'CA-IS1044S', 'CA-IS3740HB', 'CA-IS3720LW', 'IF1043', 'cs48505m', 'CAIS3730HB', 'IS3763LN',
     'CS817x22HS', 'CA-IS3742ln', 'CA-IS3021s', 'CA-IS3641LW', 'cs48520s', 'CA-IS1204w', 'CA-IS3760LW', 'CA-IF4820HD',
     'IS3720HW', 'CA-IS1044S', 'CA-IS3722LW', 'CA-IS3722LS', 'CAIS3763HN', 'IS3730HN', 'CA-IS3731LN', 'CA-IS3762lw',
     'IS3760LW', 'CA-IS3642hw', 'IS3642HW', 'IF4820HM', 'CA-IS3082WX', 'CA-IS3722hw', 'CA-IS3721HS', 'IS3086WX',
     'IF4888HS', 'CS48505D', 'CAIS3730HN', 'CA-IF1044VS Q1', 'CA-IF4805HS', 'CAIS3763HW', 'IS3742HW', 'CA-IS1200G',
     'IF428', 'CA-IS3730hw', 'IS3021W', 'CA-IS3740hn', 'IS3980P', 'CA-IS3105W', 'IS3644LW', 'CS817', 'CA-IS3643LW',
     'CA-IF4888hs', 'CAIF4820HM', 'CAIS1300G25G', 'cs817x22hs', 'CAIS3741LB', 'IS1204W', 'CAIS3721HW', 'IF1021',
     'CAIS3641LW', 'CA-IF1044vs-q1', 'CAIS3740LW', 'CA-IS3102w', 'CAIS1200U', 'CA-IS3761LW', 'CAIS3741LN',
     'CA-IS3741lw', 'IS3021S', 'CAIS3761HN', 'CA-IS3762LW', 'CA-IS3730hb', 'CA-IS3731HB', 'CS48505S', 'CA-IF1042S-Q1',
     'CA-IF1051S-Q1', 'CA-IS3741LB', 'CAIS3761LW', 'IS3643HW', 'IF4820FS', 'IS3082_88', 'IS3050U', 'CA-IS3980S',
     'IS1300B25', 'CA-IS1200u', 'IS3763HN', 'CA-IS1200U', 'CAIS3762LW', 'CA-IS1305am25w', 'CAIS3101B', 'CAIS3020W',
     'CA-IS3741lb', 'CA-IS3731HW', 'CA-IS3052W', 'CA-IS3761HN', 'CA-IS3722ls', 'CAIS3080WX', 'CA-IS3988P', 'IS398',
     'CA-IS3762LN', 'CA-IF1021S Q1', 'CAIS3050G', 'CA-IS3092W', 'CA-IF4820HS', 'CA-IS3641LW', 'CA-IS3740HB', 'AG001',
     'IF1051', 'IS3760HW', 'CA-IS3020w', 'IS3105', 'CAIS3092W', 'IS3720LG', 'CA-IF1051s-q1', 'IS3742HN', 'CAIF4820HS',
     'CA-IS3021w', 'IF1042VS-Q1', 'IS3742LW', 'CA-IS3101b', 'CA-IS3720lw', 'CA-IS1306M25G', 'CA-IS3640hw', 'CA-IS3050w',
     'IS3101B', 'CA-IF4820hm', 'CS817x20HS', 'CA-IF1051vs-q1', 'IS3761LN', 'CA-IS3763LW', 'CAIS3731HN', 'CA-IS3741hn',
     'CA-IF1051VS Q1', 'CA-IS3722HG', 'IS1200G', 'IS3641HW', 'IS3741LW', 'CA-IF4820HD', 'CA-IS3641lw', 'IS3741HN',
     'IF4850HS', 'CA-IS3741LN', 'CA-IS3741LW', 'CA-IS3080wx', 'CA-IF1051HS', 'CA-IS3020s', 'CA-IF1051VS-Q1',
     'CAIF1021SQ1', 'CA-IS3731HW', 'IS3644HW', 'CAIS3763LW', 'CA-IS3731LN', 'CAIS3740HB', 'CA-IS3021W', 'IS3721HW',
     'IS3720HG', 'CAIS3082WNX', 'CA-IS2082b', 'CA-IS3721ls', 'CA-IS3720HW', 'IS3052W', 'CA-IS3731hn', 'CA-IS3761hn',
     'CA-IS2082B', 'IF1042S-Q1', 'CAIS3762HN', 'CA-IS3722hg', 'CA-IS3731hb', 'IS3730HB', 'CAIF4888HS', 'CA-IS3052w',
     'CAIS3720HS', 'CAIS3722LG', 'IS1306', 'CA-IF4023', 'IS302', 'CAIS1044S', 'CAIF1042SQ1', 'CAIS3762HW',
     'CA-IS3721hw', 'IF1051S-Q1', 'IS3980S', 'CA-IS1044s', 'IS3640HW', 'CA-IS3720HS', 'CA-IS3761HN', 'CA-IS3086WX',
     'CAIS3742HN', 'CA-IS3722HW', 'CA-IS3086WX', 'CA-IS3742LN', 'CA-IS3641HW', 'CA-IS3642HW', 'CA-IF1044S-Q1',
     'CA-IS3052G', 'CAIF1044SQ1', 'CA-IS3052W', 'CAIS3721HS', 'CA-IS3980P', 'CA-IS3720HW', 'CA-IS3740HN', 'IS3988P',
     'CAIS3720LW', 'CA-IS3052g', 'CAIS3020S', 'cs817x20ls', 'CAIS3720LS', 'CAIS3761HW', 'CA-IS3641hw', 'CA-IS3742HN',
     'CA-IS3722LG', 'IS3721LW', 'IF1051VS-Q1', 'CAIS1305AM25W', 'CA-IS3742hn', 'CA-IS3730LN', 'cs817x20hs',
     'CA-IS3643lw', "IS384"})

critic_keywords.extend(['卓胜微', '南亚新材', '唯捷创芯', '广东生益', '思瑞浦', '浙江华正', '艾为', '金安国记'])
critic_keywords.extend(['adc12dj5200', 'adc12qj1600', 'ads131b', 'ads9815', 'afe7906', 'afe7951', 'afe882',
                         'amc131', 'awrl1432', 'dac532', 'iwrl6432', 'ldc3114', 'lmg3422', 'opt3004',
                         'pga305', 'tps272', 'tps281', 'tps8804'])

enemy_products = ['8100', '6801']
critic_keywords.extend(enemy_products)


def contains_str(input_str, keyword):
    return keyword in input_str


def get_all_file_paths(img_path):
    file_paths = []  # 初始化一个空列表，用于存储文件路径
    for dirpath, dirnames, filenames in os.walk(img_path):
        for filename in filenames:
            # 使用 os.path.join 来获取完整的文件路径
            file_path = os.path.join(dirpath, filename)
            file_paths.append(file_path)  # 将文件路径添加到列表中
    return file_paths


def get_longest_digits(keyword):
    match = re.search(r'\d+', keyword)
    if match:
        return match.group()
    else:
        return ''


def find_img(keyw: str, folder='价格手册'):
    keyword = get_longest_digits(keyw)

    # keyword = "1042"
    result = []
    # folder = "/data/lidong/fastqa/价格手册"

    for filepath in os.listdir(folder):
        fullpath = os.path.join(folder, filepath)

        if contains_str(fullpath, keyword):
            result.append(fullpath)
    return result


def find_product_img(keyw: str, folder='图片'):
    keyword = keyw

    # keyword = "1042"
    result = []
    # folder = "/data/lidong/fastqa/价格手册"

    for filepath in os.listdir(folder):
        fullpath = os.path.join(folder, filepath)

        if contains_str(fullpath, keyword):
            result.append(fullpath)
    return result


def filter_product_names(user_query, product_list):
    filter_name = []

    for product in product_list:
        if product in user_query:
            filter_name.append(product)

    return filter_name


def rank_values(multi_product):
    ranked_list = []

    # Extract the 'multi' and 'no_product' keys and values
    multi_values = multi_product.get('multi', []).copy()
    no_product_values = multi_product.get('no_product', []).copy()

    # Get the other keys
    other_keys = [key for key in multi_product.keys() if key not in ['multi', 'no_product']]

    # While there are still values in 'multi' and any of the other keys
    while multi_values or any(multi_product[key] for key in other_keys):
        if multi_values:
            ranked_list.append(multi_values.pop(0))
        for key in other_keys:
            if multi_product[key]:
                ranked_list.append(multi_product[key].pop(0))

    # Finally, add the 'no_product' values
    ranked_list.extend(no_product_values)

    return ranked_list


def filter_knowledge(question, results):

    query_list = set(filter_product_names(question, critic_keywords))

    multi_product = {}
    multi_product["multi"] = []
    multi_product["no_product"] = []
    for i in query_list:
        multi_product[i] = []

    # print("Step 1")
    all_text = ''
    if len(query_list) == 0:
        all_text = '\n\n'.join(results)
        return all_text
    else:
        for text in results:
            content_list = filter_product_names(text, query_list)
            if len(content_list) == 0:
                multi_product["no_product"].append(text.replace('[desc]', ''))
            elif len(content_list) > 1:
                multi_product["multi"].append(text.replace('[desc]', ''))
            else:
                # print("content is" + content_list[0])
                multi_product[content_list[0]].append(text.replace('[desc]', ''))
    # print("Step 2")
    rank_list = rank_values(multi_product)

    return '\n\n'.join(rank_list)

    # return '\n'.join(rank_list),img_dic
