print('——实验数据录入系统——')

sample_id = input('请输入样品编号：')
od_value = float(input('请输入OD600值:'))
dilution_factor = int(input('请输入稀释倍数:'))

od_corrected = od_value * dilution_factor

print(f'{sample_id}经过校正之后的OD600值为:{od_corrected}')
