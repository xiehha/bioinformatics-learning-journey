# OD600平均值，重新写一个
# 要求：创建一个包含 3 个数字的列表，计算总和与平均值，并用 f-string 打印出 "平均值为: X"。

OD600_values = [0.5, 0.7, 0.6]  
OD_sum = sum(OD600_values)
OD_length = len(OD600_values)
OD_average = OD_sum / OD_length if OD_length > 0 else 0
print(f'平均值为: {OD_average}')

#用input输入列表,用户输入逗号分隔的数值，代码负责切割和转换

user_input = input("请输入逗号分隔的OD600数值: ")
od_list = [float(value.strip()) for value in user_input.split(',') if value.strip()]

print(f'您输入的OD600数值为: {od_list}')
print(f'总和为: {sum(od_list)}')
