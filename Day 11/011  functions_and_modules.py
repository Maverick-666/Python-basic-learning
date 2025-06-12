# day_14_functions_and_modules.py

import math # For factorial example and other math functions
from random import randrange # For roll_dice example
import timeit # For module from previous lesson, just to ensure it runs if any code was copied

# -----------------------------------------------------------------------------
# 引入问题：计算组合数 C(m,n) = m! / (n! * (m-n)!)
# 原始版本 - 重复代码
# -----------------------------------------------------------------------------
print("--- 组合数计算 (原始版) ---")
# m_orig = 7 # int(input('m = '))
# n_orig = 3 # int(input('n = '))

# fm_orig = 1
# for num_orig in range(1, m_orig + 1):
#     fm_orig *= num_orig
# fn_orig = 1
# for num_orig in range(1, n_orig + 1):
#     fn_orig *= num_orig
# fk_orig = 1
# for num_orig in range(1, m_orig - n_orig + 1):
#     fk_orig *= num_orig
# print(f"C({m_orig},{n_orig}) original: {fm_orig // fn_orig // fk_orig}")
# print("\n")

# -----------------------------------------------------------------------------
# 一、定义函数 (Defining Functions)
# - 使用 `def` 关键字。
# - 函数名、参数 (自变量)、返回值 (因变量)。
# - `return` 语句返回值，若无则返回 `None`。
# - 函数体通过缩进定义。
# -----------------------------------------------------------------------------
print("--- 1. 定义函数 ---")

# 1.1 将求阶乘操作封装到函数中
def factorial_custom(num):
    """计算非负整数num的阶乘 (自定义版本)"""
    if not isinstance(num, int) or num < 0:
        # 一般会抛出异常，这里简单返回错误提示或0
        print("Error: Input must be a non-negative integer.")
        return 0 # 或者 raise ValueError(...)
    result = 1
    for n_val in range(1, num + 1): # range(1,1) is empty, so 0! = 1 correctly
        result *= n_val
    return result

# 使用自定义函数计算组合数
m_func_d14 = 7
n_func_d14 = 3
# print(f"Input m = {m_func_d14}, n = {n_func_d14}")
combinations_custom = factorial_custom(m_func_d14) // \
                      factorial_custom(n_func_d14) // \
                      factorial_custom(m_func_d14 - n_func_d14)
print(f"C({m_func_d14},{n_func_d14}) using custom factorial_custom(): {combinations_custom}")

# 1.2 使用 math 模块的 factorial 函数
# from math import factorial # 已经在文件顶部导入
combinations_math = math.factorial(m_func_d14) // \
                    math.factorial(n_func_d14) // \
                    math.factorial(m_func_d14 - n_func_d14)
print(f"C({m_func_d14},{n_func_d14}) using math.factorial(): {combinations_math}")

# 1.3 导入函数时使用别名 (as)
from math import factorial as f_alias
combinations_alias = f_alias(m_func_d14) // \
                     f_alias(n_func_d14) // \
                     f_alias(m_func_d14 - n_func_d14)
print(f"C({m_func_d14},{n_func_d14}) using aliased factorial (f_alias): {combinations_alias}")
print("\n")

# -----------------------------------------------------------------------------
# 二、函数的参数 (Function Arguments/Parameters)
# -----------------------------------------------------------------------------
print("--- 2. 函数的参数 ---")

# 2.1 位置参数和关键字参数
def can_form_triangle_pos(a, b, c):
    """判断三条边能否构成三角形 (位置参数)"""
    # print(f"Checking triangle with sides: a={a}, b={b}, c={c}")
    return a + b > c and b + c > a and a + c > b

print(f"can_form_triangle_pos(1, 2, 3): {can_form_triangle_pos(1, 2, 3)}")  # False
print(f"can_form_triangle_pos(4, 5, 6): {can_form_triangle_pos(4, 5, 6)}")  # True
# 使用关键字参数调用
print(f"can_form_triangle_pos(b=2, c=3, a=1): {can_form_triangle_pos(b=2, c=3, a=1)}") # False

# 2.2 强制位置参数 (/) (Python 3.8+)
def can_form_triangle_pos_only(a, b, c, /):
    """判断三条边能否构成三角形 (强制位置参数)"""
    return a + b > c and b + c > a and a + c > b
print(f"can_form_triangle_pos_only(3,4,5): {can_form_triangle_pos_only(3,4,5)}") # True
# print(can_form_triangle_pos_only(a=3,b=4,c=5)) # TypeError

# 2.3 命名关键字参数 (*)
def can_form_triangle_kw_only(*, a, b, c):
    """判断三条边能否构成三角形 (命名关键字参数)"""
    return a + b > c and b + c > a and a + c > b
print(f"can_form_triangle_kw_only(a=3,b=4,c=5): {can_form_triangle_kw_only(a=3,b=4,c=5)}") # True
# print(can_form_triangle_kw_only(3,4,5)) # TypeError

# 2.4 参数的默认值
# from random import randrange # 已经在文件顶部导入
def roll_dice_default(num_dice=2):
    """模拟摇num_dice颗骰子，返回点数和。默认2颗。"""
    total_points = 0
    for _ in range(num_dice):
        total_points += randrange(1, 7)
    return total_points

print(f"roll_dice_default(): {roll_dice_default()}")       # 使用默认值 num_dice=2
print(f"roll_dice_default(3): {roll_dice_default(3)}")   # 传入参数 num_dice=3

def add_default(a=0, b=0, c=0):
    """三个数相加，参数有默认值"""
    return a + b + c
print(f"add_default(): {add_default()}")             # 0
print(f"add_default(1): {add_default(1)}")           # 1
print(f"add_default(1, 2): {add_default(1, 2)}")     # 3
print(f"add_default(1, 2, 3): {add_default(1, 2, 3)}") # 6
# def wrong_order(a=0, b): return a+b # SyntaxError: non-default argument follows default argument

# 2.5 可变参数 (*args 和 **kwargs)
# *args: 接收任意多个位置参数，打包成一个元组 (tuple)
def add_variable_pos(*args_tuple):
    """对传入的所有数值型参数求和"""
    total_sum_var = 0
    # print(f"Received args_tuple: {args_tuple}")
    for val_var in args_tuple:
        if isinstance(val_var, (int, float)): # 更推荐用isinstance进行类型检查
            total_sum_var += val_var
    return total_sum_var

print(f"add_variable_pos(): {add_variable_pos()}")                 # 0
print(f"add_variable_pos(1, 2, 3): {add_variable_pos(1, 2, 3)}")      # 6
print(f"add_variable_pos(1, 2.5, 'text', 4): {add_variable_pos(1, 2.5, 'text', 4)}") # 7.5

# **kwargs: 接收任意多个关键字参数，打包成一个字典 (dict)
def process_info(*args_info, **kwargs_info):
    """演示*args和**kwargs"""
    print(f"Positional arguments (*args_info): {args_info}")
    print(f"Keyword arguments (**kwargs_info): {kwargs_info}")

process_info(10, 'hello', status=True, user='admin', attempts=3)
# Positional arguments: (10, 'hello')
# Keyword arguments: {'status': True, 'user': 'admin', 'attempts': 3}
print("\n")

# -----------------------------------------------------------------------------
# 三、用模块管理函数 (Modules)
# - 每个 .py 文件就是一个模块。
# - 解决命名冲突。
# - 组织代码。
# -----------------------------------------------------------------------------
print("--- 3. 用模块管理函数 ---")
# 假设存在 module1.py 和 module2.py 文件:
# module1.py:
# def foo():
#     print('Output from module1.foo()')

# module2.py:
# def foo():
#     print('Output from module2.foo()')

# 在当前文件 (或一个 test.py) 中:
# import module1_example as m1 # 假设我们创建了这些文件
# import module2_example as m2
# m1.foo()
# m2.foo()

# from module1_example import foo as foo1
# from module2_example import foo as foo2
# foo1()
# foo2()
print("模块管理示例见原文，需创建额外.py文件运行。")
print("核心思想：import module_name; module_name.function()")
print("或者：from module_name import function_name [as alias]")
print("\n")

# -----------------------------------------------------------------------------
# 四、标准库中的模块和函数
# - Python自带大量有用模块 (e.g., math, random, time, os, sys, json, re)
# - 内置函数 (Built-in Functions): 无需导入即可直接使用。
# -----------------------------------------------------------------------------
print("--- 4. 标准库与内置函数 ---")
print("部分内置函数示例:")
print(f"abs(-5.5): {abs(-5.5)}")               # 5.5
print(f"bin(10): {bin(10)}")                 # 0b1010
print(f"chr(65): {chr(65)}")                 # A
print(f"hex(255): {hex(255)}")               # 0xff
# val_input = input("Enter something: ") # 示例中跳过实际输入
# print(f"You entered: {val_input}")
print(f"len('python'): {len('python')}")         # 6
print(f"max(10, 30, 20): {max(10, 30, 20)}")     # 30
print(f"min([5, 2, 8]): {min([5, 2, 8])}")       # 2 (可迭代对象)
print(f"oct(10): {oct(10)}")                 # 0o12
# open() - 文件操作，此处不演示
print(f"ord('A'): {ord('A')}")                 # 65
print(f"pow(2, 5): {pow(2, 5)}")               # 32
# print() - 已广泛使用
print(f"list(range(3)): {list(range(3))}")     # [0, 1, 2]
print(f"round(3.14159, 2): {round(3.14159, 2)}") # 3.14
print(f"sum([1, 2, 3, 4]): {sum([1, 2, 3, 4])}") # 10
print(f"type(123): {type(123)}")             # <class 'int'>
print(f"type('abc'): {type('abc')}")           # <class 'str'>
print("\n")

print("--- End of Day 14 Functions and Modules Demo ---")