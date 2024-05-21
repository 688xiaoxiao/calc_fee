import os

# 固定的文件上层目录路径
base_folder_path = r"D:\Files\Reimburse"

folder_name_template = "4.11 - 4.19\n"
print(f"示例文件夹名称：{folder_name_template}")

user_input_folder_name = input("请输入文件夹名称：")
print("\n")
target_folder_path = os.path.join(base_folder_path, user_input_folder_name)


def get_invoice_total_amount(folder_path):
    accommodation_amount = 0 
    taxi_fares = 0
    other_taxi_fares = 0
    # food_amount = 0

    for _, _, file_names in os.walk(folder_path):
        for file_name in file_names:
            if "住宿发票" in file_name:
                amount_str = file_name.split(' ')[-2].split("元")[0]  # 要求文件名包含金额，以空格分隔  格式为 日期 金额元 住宿发票.后缀名
                accommodation_amount += float(amount_str)

            elif "打车电子发票" in file_name:
                amount_str = file_name.split('元')[0].split('-')[-1]
                taxi_fares += float(amount_str)

            elif "到" in file_name:
                amount_str = file_name.split('元')[0].split(' ')[-1]
                other_taxi_fares += float(amount_str)

    total_amount = accommodation_amount + taxi_fares +  other_taxi_fares
    transportation_amount = taxi_fares +  other_taxi_fares
    return accommodation_amount, transportation_amount, total_amount

accommodation_amount, transportation_amount, total = get_invoice_total_amount(target_folder_path)
print(f"{user_input_folder_name} 的报销金额计算如下：\n")

print(f"▶ 住宿总金额: {accommodation_amount}元")
print(f"▶ 交通总金额: {transportation_amount}元\n")
# print(f"餐补总金额: {food_amount}元")
print(f"▶▶▶ 住宿 + 交通 报销总金额: {total}元\n")
for i in [0, 1, 2]:
    print("请自行计算 【餐补总金额】，谢谢！")
print(" ")
print(" ")
