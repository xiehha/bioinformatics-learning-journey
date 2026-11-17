sample_name = 'A01'
condition = 'Control'
OD600 = 0.18
dilution_factor = 1
corrected_OD600 = OD600 * dilution_factor
print('样本名称：', sample_name)
print('条件：', condition)
print('OD600:', OD600)
print('稀释因子：', dilution_factor)
print('校正后的OD600:', corrected_OD600)