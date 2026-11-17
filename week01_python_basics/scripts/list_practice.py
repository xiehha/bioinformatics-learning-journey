all_od_value = [0.18,0.21,0.19,0.22,0.2,0.31,0.34,0.29,0.33,0.32]

print(f'第一个数据是：{all_od_value[0]}')
print(f'第二个数据是：{all_od_value[1]}')
print(f'最后一个数据是：{all_od_value[-1]}')

print(f'现在的数据长度是：{len(all_od_value)}')

all_od_value.append(0.28)

print(f'添加一个数据后，最后一个数据是：{all_od_value[-1]}')
print(f'现在的数据长度是：{len(all_od_value)}')