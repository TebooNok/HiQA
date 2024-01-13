import csv

# 输入文件路径和输出文件路径
input_file_path = "others_products.csv"
output_file_path = "others_products_new.csv"

# 用于存储型号的变量
model = None

# 打开输入文件以读取CSV数据
with open(input_file_path, newline='', encoding='gbk') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

    # 查找并提取型号
    for row in rows:
        if "川土微公司芯片产品料号：" in row[0]:
            model = row[0].split("\n")[2].strip().split("：")[1].strip()
            # break
            print(model)
            title = row[0].split('\n')[0]
            content = '\n'.join(row[0].split('\n')[1:])
            new_title = title.replace("[desc] 川土微芯片产品", '')
            new_title = f"[desc] 川土微芯片产品：{model} {new_title}"
            row[0] = new_title + '\n' + content

# 保存处理后的数据为UTF-8编码的CSV文件
with open(output_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

print("处理完成，结果已保存到", output_file_path)
