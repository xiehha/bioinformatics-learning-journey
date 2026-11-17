OD600_control = [0.18,0.21,0.19,0.22,0.2]
length_control = len(OD600_control)
OD600_control_sum = sum(OD600_control)
OD600_average = OD600_control_sum / length_control
print('对照组数据的OD600值为:',OD600_control)
print('OD600总和为:',OD600_control_sum)
print('数据总数为:',length_control)
print('OD600的平均值为:',OD600_average)

OD600_treatment = [0.31,0.34,0.29,0.33,0.32]
length_treatment = len(OD600_treatment)
OD600_treatment_sum = sum(OD600_treatment)
OD600_treatment_average = OD600_treatment_sum / length_treatment
print('处理组数据的OD600值为:',OD600_treatment)
print('OD600总和为:',OD600_treatment_sum)
print('数据总数为:',length_treatment)
print('OD600的平均值为:',OD600_treatment_average)