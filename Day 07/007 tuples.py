# day_10_tuples.py

import timeit

# -----------------------------------------------------------------------------
# 核心概念：元组 (Tuple)
# - 多个元素按照一定顺序构成的序列。
# - 不可变类型 (immutable): 一旦定义，元素不能添加、删除或修改值。
# - 定义通常使用 () 字面量语法。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、元组的定义和运算
# -----------------------------------------------------------------------------
print("--- 1. 元组的定义和运算 ---")

# 1.1 定义元组
t1_d10 = (35, 12, 98)  # 三元组
t2_d10 = ('骆昊', 45, True, '四川成都') # 四元组 (原文43，改为45以匹配后续输出)
print(f"t1_d10: {t1_d10}, type: {type(t1_d10)}")
print(f"t2_d10: {t2_d10}, type: {type(t2_d10)}")

# 1.2 元组的属性和基本运算 (与列表类似)
print(f"Length of t1_d10: {len(t1_d10)}") # 3
print(f"t1_d10[0]: {t1_d10[0]}")           # 35
print(f"t2_d10[-1]: {t2_d10[-1]}")        # 四川成都
print(f"Slice t2_d10[:2]: {t2_d10[:2]}")  # ('骆昊', 45)
print(f"Slice t2_d10[::3]: {t2_d10[::3]}")# ('骆昊', '四川成都')

print("\nLooping through t1_d10:")
for elem_d10 in t1_d10:
    print(elem_d10, end=" ") # 35 12 98
print()

print(f"\n12 in t1_d10: {12 in t1_d10}")             # True
print(f"'Hao' not in t2_d10: {'Hao' not in t2_d10}") # True

t3_d10 = t1_d10 + t2_d10 # 拼接
print(f"t3_d10 (t1 + t2): {t3_d10}")
# (35, 12, 98, '骆昊', 45, True, '四川成都')

print(f"t1_d10 == (35, 12, 98): {t1_d10 == (35, 12, 98)}") # True
print(f"t1_d10 < (35, 12, 100): {t1_d10 < (35, 12, 100)}") # True

# 1.3 不可变性演示 (尝试修改会报错)
# t1_d10[0] = 100  # TypeError: 'tuple' object does not support item assignment
# t1_d10.append(50) # AttributeError: 'tuple' object has no attribute 'append'

# 1.4 特殊元组定义：空元组和一元组
empty_tuple_d10 = ()
print(f"\nEmpty tuple: {empty_tuple_d10}, type: {type(empty_tuple_d10)}")

not_a_tuple1_d10 = ('hello') # This is a string
not_a_tuple2_d10 = (100)     # This is an int
print(f"('hello') type: {type(not_a_tuple1_d10)}")
print(f"(100) type: {type(not_a_tuple2_d10)}")

single_element_tuple1_d10 = ('hello',) # Note the comma
single_element_tuple2_d10 = (100,)    # Note the comma
print(f"('hello',) type: {type(single_element_tuple1_d10)}")
print(f"(100,) type: {type(single_element_tuple2_d10)}")
print("\n")

# -----------------------------------------------------------------------------
# 二、打包和解包操作 (Packing and Unpacking)
# -----------------------------------------------------------------------------
print("--- 2. 打包和解包操作 ---")

# 2.1 打包 (Packing)
# 多个用逗号分隔的值赋给一个变量时，会自动打包成元组
packed_tuple_d10 = 1, 10, 100
print(f"Packed tuple: {packed_tuple_d10}, type: {type(packed_tuple_d10)}") # (1, 10, 100)

# 2.2 解包 (Unpacking)
# 将元组/序列赋值给多个变量时，元组会解包
i_d10, j_d10, k_d10 = packed_tuple_d10
print(f"Unpacked: i={i_d10}, j={j_d10}, k={k_d10}") # 1 10 100

# 2.3 解包时元素个数与变量个数不匹配 (会报错)
# mismatched_tuple_d10 = 1, 10, 100, 1000
# l, m, n = mismatched_tuple_d10 # ValueError: too many values to unpack
# l, m, n, o, p = packed_tuple_d10 # ValueError: not enough values to unpack

# 2.4 使用星号表达式 (*) 解包
# - 用星号修饰的变量会变成一个列表，接收剩余的元素。
# - 星号表达式在解包中只能出现一次。
print("\n--- 2.4 星号表达式解包 ---")
star_tuple_d10 = 1, 10, 100, 1000, 2000
x1, y1, *z1 = star_tuple_d10
print(f"x1, y1, *z1: x1={x1}, y1={y1}, z1={z1} (type: {type(z1)})") # z1 is [100, 1000, 2000]

x2, *y2, z2 = star_tuple_d10
print(f"x2, *y2, z2: x2={x2}, y2={y2}, z2={z2}") # y2 is [10, 100, 1000]

*x3, y3, z3 = star_tuple_d10
print(f"*x3, y3, z3: x3={x3}, y3={y3}, z3={z3}") # x3 is [1, 10, 100]

x4, y4, z4, *l4 = star_tuple_d10 # l4 is [1000, 2000]
print(f"x4,y4,z4,*l4: x4={x4}, y4={y4}, z4={z4}, l4={l4}")

x5, y5, z5, l5, *m5 = star_tuple_d10 # m5 is [2000]
print(f"x5,y5,z5,l5,*m5: x5={x5}, y5={y5}, z5={z5}, l5={l5}, m5={m5}")

x6, y6, z6, l6, m6, *n6 = star_tuple_d10 # n6 is []
print(f"x6,y6,z6,l6,m6,*n6: x6={x6},y6={y6},z6={z6},l6={l6},m6={m6},n6={n6}")

# 2.5 解包适用于所有序列
print("\n--- 2.5 解包其他序列 ---")
r1, r2, *r3 = range(1, 6) # range(1, 6) is 1, 2, 3, 4, 5
print(f"Unpacking range: r1={r1}, r2={r2}, r3={r3}") # r1=1, r2=2, r3=[3, 4, 5]

s1, *s2, s3 = 'python'
print(f"Unpacking string: s1={s1}, s2={s2}, s3={s3}") # s1='p', s2=['y', 't', 'h', 'o'], s3='n'
print("\n")

# -----------------------------------------------------------------------------
# 三、交换变量的值
# Python 中交换变量非常简洁，不一定需要打包解包，有字节码指令支持。
# -----------------------------------------------------------------------------
print("--- 3. 交换变量的值 ---")
var_a_d10 = 100
var_b_d10 = 200
print(f"Before swap: var_a={var_a_d10}, var_b={var_b_d10}")
var_a_d10, var_b_d10 = var_b_d10, var_a_d10 # ROT_TWO bytecode instruction
print(f"After swap: var_a={var_a_d10}, var_b={var_b_d10}")

var_c_d10 = 300
print(f"Before 3-var swap: a={var_a_d10}, b={var_b_d10}, c={var_c_d10}")
# a becomes b, b becomes c, c becomes a
var_a_d10, var_b_d10, var_c_d10 = var_b_d10, var_c_d10, var_a_d10 # ROT_THREE
print(f"After 3-var swap: a={var_a_d10}, b={var_b_d10}, c={var_c_d10}")
print("\n")

# -----------------------------------------------------------------------------
# 四、元组和列表的比较
# -----------------------------------------------------------------------------
print("--- 4. 元组和列表的比较 ---")
# 4.1 不可变性 (Immutability)
# - 元组不可变，适合多线程环境，减少同步开销。

# 4.2 创建时间比较 (元组通常更快)
# 使用 timeit 模块进行性能测试
# (结果因系统而异，原文显示元组创建更快)
# print("Timing list creation vs tuple creation (10,000,000 times):")
# list_creation_time = timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=1000000) # Reduced number for faster demo
# tuple_creation_time = timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=1000000)
# print(f'List creation: {list_creation_time:.3f} 秒 (for 1,000,000 ops)')
# print(f'Tuple creation: {tuple_creation_time:.3f} 秒 (for 1,000,000 ops)')
# (注：实际运行时间差异可能受Python版本、系统等多种因素影响)

# 4.3 类型转换
print("\n--- 4.3 类型转换 ---")
infos_tuple_d10 = ('骆昊', 45, True, '四川成都')
infos_list_d10 = list(infos_tuple_d10) # 元组转列表
print(f"Tuple to list: {infos_list_d10}, type: {type(infos_list_d10)}")

fruits_list_d10 = ['apple', 'banana', 'orange']
fruits_tuple_d10 = tuple(fruits_list_d10) # 列表转元组
print(f"List to tuple: {fruits_tuple_d10}, type: {type(fruits_tuple_d10)}")
print("\n")

# -----------------------------------------------------------------------------
# 五、总结 (来自原文)
# - 列表和元组都是有序容器。
# - 列表可变，元组不可变。
# - 列表有添加、删除、排序等修改操作，元组没有。
# - 两者都支持拼接、成员、索引、切片运算。
# - 字符串也支持这些序列运算。
# -----------------------------------------------------------------------------

print("--- End of Day 10 Tuples Demo ---")