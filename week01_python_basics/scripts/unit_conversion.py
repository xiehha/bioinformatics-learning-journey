# 单位换算
#要求：定义一个变量 mass_mg = 500（毫克），将它换算成克（g），并打印结果。公式：1 g = 1000 mg。

mass_mg = float(input('请输入毫克数：'))

mass_g = mass_mg / 1000

print(f'{mass_mg}毫克等于{mass_g}克')


