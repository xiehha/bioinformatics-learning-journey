# Day1
>VS Code是源代码编辑器和轻量级集成开发环境，核心功能是提供文本编辑、语法高亮、代码折叠、版本控制集成等，本身确实不具备执行 Python 代码的能力。

>python.exe是解释器（Interpreter）。读取你写的 .py 源文件，将其编译为字节码，然后交由 Python 虚拟机（PVM）在操作系统层面执行。

>VS Code 的 Python 插件充当了客户端与调试器的桥梁。它负责向 VS Code 提供代码补全、静态检查，并在你点击“运行”时，通过 subprocess 调用底层的解释器（python.exe）来执行脚本。
VS code里选择某个环境下的python的方法：VS code里按 Ctrl + Shift + P 直接选或者输入路径就行。

>Conda 是一个包和环境管理器。它允许在同一个操作系统下，隔离出多个独立的 Python 运行环境（如 base、bioenv）。每个环境都有自己独立的 python.exe 和依赖库，互不干扰。

>print()是Pytho 的内置函数，负责将传入的参数对象转换为字符串（调用对象的 __str__ 方法），并输出到标准输出流,通常是你的终端或控制台，最后默认追加一个换行符。

>❗❗❗f-string（Formatted String Literal）是 Python 3.6 引入的一种字符串格式化机制。通过在字符串前加前缀 f 或 F，允许在字符串内部直接嵌入 Python 表达式。
表达式求值：字符串中的大括号 {} 作为占位符。Python 解释器在运行时会对 {} 内的内容进行求值。
{} 内部不仅可以填入变量名，还可以填入算术表达式（如 {1 + 2}）或函数调用（如 {len(values)}）。
求值后的结果会被自动转换为字符串类型，并替换原来的大括号区域。

>字符串（str） - 用引号包起来的文字
浮点数(flaot) - 带小数点的数字
整数(int) - 没有小数点的数字
布尔值(bool) - 只有 True 和 False

>**乘方、//整除、%取余数

>len()计算列表里有几个数据

# Day2
>列表的索引（Index）是从 0 开始的
第 1 个元素：列表名[0]
第 2 个元素：列表名[1]
最后一个元素：列表名[-1] （在 Python 里，负数代表从后往前数）

>append()向列表里添加数据

>input函数：从标准输入流（通常指终端或控制台）读取一行文本。遇到回车符（Enter）时停止读取并返回。
程序执行到 input() 时会暂停（阻塞），直到用户提供输入。
无论用户输入的是数字还是文字，input() 的返回值始终是字符串（str）类型。

✅python里需要空格的情况：
（1）语法强制要求的空格：缩进（Indentation）
在 if、else、for 等语句下方的分支代码，必须向右缩进 4 个空格。
注意：行首绝不能随便多打空格，否则 Python 就会报缩进错误。

（2）规范建议的空格：可读性空格（PEP 8 标准）
赋值号两侧：a = 1（对），a=1（不规范）。
算术运算符两侧：a + b（对），a+b（不规范）。
逗号后面：[1, 2, 3]（对），[1,2,3]（不规范）。
函数参数内部和括号前：print(a, b)（对），print (a, b)（不规范）。
小建议：在 VS Code 里按 Shift + Alt + F，它可以一键把格式排得漂亮。

✅python的三种括号
（1）圆括号()--调用、分组、元组
a.函数调用（Function Call）（最常用）：当你看到 () 紧跟在某个单词后面，意味着你在“执行”这个函数。
例如：print("Hello")、input()、float("0.18")、len(values)。括号里放的是传给函数的参数（Arguments）。
b.数学运算分组（Grouping）：改变运算优先级，和数学里的括号一样。
例如：(1 + 2) * 3 （先算加法，再算乘法）。
c.元组（Tuple）：一种不可变的序列，用来存放多个数据。元组一旦创建，里面的元素就不能修改
例如：coordinates = (30.5, 114.3)。

（2）方括号[]--列表与索引
a.定义列表（List）：创建一种可以修改、有序的序列。
例如：od_values = [0.18, 0.21, 0.19]。
b.索引与切片（Indexing & Slicing）：从序列（字符串、列表等）中“提取”特定位置的数据。
例如：od_values[0]（提取第 1 个元素）、od_values[-1]（提取最后一个元素）。

（3）花括号{}--字典与集合 (以及 f-string)
a.字典（Dictionary）：用来存储“键值对（Key-Value）”数据。这是生信里最常用的数据结构之一（比如把基因名映射到表达量）。字典是可变的。
例如：gene_vaf = {"EGFR": 0.45, "KRAS": 0.12}。
b.集合（Set）：一种无序且不包含重复元素的序列。
例如：unique_genes = {"EGFR", "TP53", "KRAS"}。
c.f-string 占位符：你在格式化字符串时使用的 {变量名} 也是花括号。
例如：print(f"平均值是: {average_od}")。

>input语法输入列表
[表达式 for 元素 in 可迭代对象 if 条件]
```bash
user_input = input("请输入逗号分隔的OD600数值: ")
od_list = [float(value.strip()) for value in user_input.split(',') if value.strip()]
```

可以先理解这个代码
```bash
od_lists = [float(x) for x in user_input.split(",")]
```

value的意思是对于（for）在（in）切分好的列表里面的每一个元素，我们把它叫作 value，然后依次拿出来处理。

第一步：切割 user_input.split(',')
把用户输入的整段字符串，按逗号切分成一个字符串列表。
比如输入 "0.1, 0.2,,0.3"，切割后变成 ['0.1', ' 0.2', '', '0.3']。

在 Python 里，它是字符串（str）自带的一个方法（技能）。

一句话解释：split() 就是拿着一把“刀”，把一长串文本，按照你指定的“标记”切成好几段，然后打包成一个列表（List）返回给你。

第二步：条件过滤 if value.strip()

.strip() 是字符串的方法，用来去除字符串开头和结尾的空格、换行符。在 Python 的字符串里，strip的作用是：去除字符串开头和结尾的“空白字符”。

如果遇到刚才那种连续逗号产生的空字符串 ''，''.strip() 还是空字符串。

在 Python 里，空字符串的布尔值是 False。所以 if value.strip() 把空字符串直接扔掉，只放行有真实数字的项。

第三步：清洗与转换 float(value.strip())
对于通过安检的元素（比如 ' 0.2'）：

先执行 value.strip() 去掉前后的空格，变成 '0.2'。

再套上 float()，将其变成真正的浮点数 0.2。

 第四步：组装成新列表
最终，所有转换好的浮点数被方括号 [] 收集起来，组成最终的 od_list。


这段代码的完整版是：

先把用户输入切分好
```bash
splitted_list = user_input.split(',') 
```
假设 user_input 是 "0.18, 0.21, 0.22"，此时 splitted_list 是 ['0.18', ' 0.21', ' 0.22']

```bash
od_list = [] # 准备一个空列表用来装结果
```

开始普通的 for 循环
```bash
for value in splitted_list:  # 依次把 '0.18'、' 0.21' 等拿出来，叫它 value
    if value.strip():        # 如果去掉空格后，不是空字符串（过滤掉空值）
        clean_value = value.strip() # 去掉两边的空格
        final_number = float(clean_value) # 把文字变成小数
        od_list.append(final_number) # 把得到的小数塞进结果列表里

print(od_list) 
```
>函数 (Function) vs 方法 (Method)
函数是“全局的公共工具”：比如 len()、print()、float()。你可以把任何东西丢进去用。语法是：函数名(参数)。例如：len("abc")
方法是“某个对象自带的专属技能”：它只属于特定的数据类型（比如字符串或列表）。语法是：对象.方法名()。例如："abc".upper()（把字符串变大写）、[1, 2].append(3)（往列表里加东西）。
点号 . 在 Python 里代表“的”。user_input.strip() 翻译成大白话就是：“调用 user_input 这个字符串的 strip 技能”。

# 踩坑
- 第2天：在用input给变量赋值的时候，多用了空格，导致语法出错
mass_g = float input('请输入以克为单位的数值：') ❌
mass_g = float(input('请输入以克为单位的数值：')) ✅
因为float()是一起的，表示函数的调用，（）表示传参

# 思考与总结
当代码里计算遇到除法的时候，要分类思考是否会出现分母为0的情况，用if else的语句
