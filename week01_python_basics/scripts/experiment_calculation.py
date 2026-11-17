# 实验数据计算
# 自己设定 样本总浓度 和 所需浓度，计算稀释倍数（总浓度 / 所需浓度），并输出结果。

sample_total_concentration = float(input("请输入样本总浓度（mg/mL）："))
desired_concentration = float(input("请输入所需浓度（mg/mL）："))

if desired_concentration <= 0:
    print("所需浓度必须大于零。")
else:
    dilution_factor = sample_total_concentration / desired_concentration
    print(f"稀释倍数为: {dilution_factor}")