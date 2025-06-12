# day_15_advanced_functions.py

import random
import time
from functools import wraps, lru_cache
import sys

# -----------------------------------------------------------------------------
# 一、装饰器 (Decorators)
# - 目的：用一个函数装饰另外一个函数并为其提供额外的能力。
# - 本质：一个高阶函数，其参数是被装饰的函数，返回值是一个带有装饰功能的函数。
# -----------------------------------------------------------------------------
print("--- 1. 装饰器 ---")

# 1.1 基础函数 (无装饰器)
def download_original(filename):
    """下载文件（原始版本）"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 0.2) # 减少休眠时间便于快速演示
    print(f'{filename}下载完成.')
    return f"{filename} downloaded successfully."

def upload_original(filename):
    """上传文件（原始版本）"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 0.3) # 减少休眠时间
    print(f'{filename}上传完成.')
    return f"{filename} uploaded successfully."

print("\n--- 1.1.1 原始函数调用 ---")
download_original('MySQL从删库到跑路.avi')
upload_original('Python从入门到住院.pdf')

# 1.2 手动添加计时功能 (重复代码)
print("\n--- 1.1.2 手动计时 (重复代码) ---")
start_manual = time.time()
download_original('Manual_Time_Test.doc')
end_manual = time.time()
print(f'手动计时花费时间: {end_manual - start_manual:.3f}秒')

# 1.3 定义装饰器函数 record_time
def record_time_decorator(func_to_decorate):
    """记录函数执行时间的装饰器"""
    @wraps(func_to_decorate) # 保留原函数的元信息 (如__name__, __doc__)
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start_time = time.time()
        # 执行被装饰的函数并获取返回值
        result_from_func = func_to_decorate(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end_time = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'--- {func_to_decorate.__name__} 执行时间: {end_time - start_time:.3f}秒 ---')
        # 返回被装饰函数的返回值
        return result_from_func
    return wrapper

# 1.4 使用装饰器的方式一：直接调用装饰器
print("\n--- 1.4.1 使用装饰器 (方式一) ---")
# download_decorated_manual = record_time_decorator(download_original)
# upload_decorated_manual = record_time_decorator(upload_original)
# download_decorated_manual('Decorated_Manually_DL.zip')
# upload_decorated_manual('Decorated_Manually_UL.rar')

# 1.5 使用装饰器的方式二：@语法糖
print("\n--- 1.4.2 使用装饰器 (@语法糖) ---")
@record_time_decorator
def download_with_decorator(filename):
    """下载文件（带装饰器）"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 0.1)
    print(f'{filename}下载完成.')
    return f"{filename} downloaded via decorator."

@record_time_decorator
def upload_with_decorator(filename):
    """上传文件（带装饰器）"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 0.15)
    print(f'{filename}上传完成.')
    return f"{filename} uploaded via decorator."

download_with_decorator('Decorated_Sugar_DL.txt')
upload_with_decorator('Decorated_Sugar_UL.md')

# 1.6 使用 @wraps 保留原函数信息，并通过 __wrapped__ 调用原函数
print("\n--- 1.5 调用被装饰前的原函数 (__wrapped__) ---")
# download_with_decorator 已经被装饰了
print("Calling decorated download_with_decorator:")
download_with_decorator('Wrapped_Test_DL.jpg')

print("\nCalling original function via __wrapped__ (no timing):")
if hasattr(download_with_decorator, '__wrapped__'):
    download_with_decorator.__wrapped__('Original_Via_Wrapped.png')
else:
    print("Could not access __wrapped__ (perhaps @wraps was not used).")
print("\n")

# 装饰器函数本身也可以参数化 (本单元未详细展开，此处不演示)

# -----------------------------------------------------------------------------
# 二、递归调用 (Recursion)
# - 函数直接或间接调用自身。
# - 需要递归收敛条件 (base case) 和递归公式 (recursive step)。
# - 注意栈溢出风险 (RecursionError)。
# -----------------------------------------------------------------------------
print("--- 2. 递归调用 ---")

# 2.1 阶乘示例
def factorial_recursive(num):
    """计算非负整数的阶乘 (递归)"""
    if not isinstance(num, int) or num < 0:
        raise ValueError("阶乘只为非负整数定义")
    if num in (0, 1): # 收敛条件 (基本情况)
        return 1
    return num * factorial_recursive(num - 1) # 递归公式

print(f"5! = {factorial_recursive(5)}") # 120
# print(factorial_recursive(5000)) # RecursionError: maximum recursion depth exceeded

# 获取和设置递归深度限制 (仅作演示，不推荐随意修改)
# original_recursion_limit = sys.getrecursionlimit()
# print(f"Original recursion limit: {original_recursion_limit}")
# sys.setrecursionlimit(6000)
# print(f"New recursion limit: {sys.getrecursionlimit()}")
# try:
#     print(f"5000! (with increased limit - may still be slow/error): {factorial_recursive(5000)}")
# except RecursionError as e:
#     print(f"Error calculating 5000!: {e}")
# sys.setrecursionlimit(original_recursion_limit) # 恢复原始限制

# 2.2 斐波那契数列示例 (递归，无优化)
def fibonacci_recursive_unoptimized(n):
    """计算第n个斐波那契数 (递归，未优化) F(1)=1, F(2)=1"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("斐波那契数列的项数必须是正整数")
    if n in (1, 2): # 收敛条件
        return 1
    return fibonacci_recursive_unoptimized(n - 1) + fibonacci_recursive_unoptimized(n - 2) # 递归公式

print("\n--- 2.2.1 Fibonacci (unoptimized recursive) ---")
print("First 10 Fibonacci numbers (unoptimized):")
for i_fib_unopt in range(1, 11): # 计算前10个，更多会非常慢
    print(f"F({i_fib_unopt}) = {fibonacci_recursive_unoptimized(i_fib_unopt)}")

# 2.3 斐波那契数列 (循环递推，更优)
def fibonacci_iterative(n):
    """计算第n个斐波那契数 (循环递推) F(0)=0, F(1)=1 -> F(n)"""
    if not isinstance(n, int) or n < 0: # 允许计算F(0)
        raise ValueError("斐波那契数列的项数必须是非负整数")
    if n == 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(n - 1): # 因为已经有了F(1)=b=1，所以再迭代 n-1 次
        a, b = b, a + b
    return b

print("\n--- 2.2.2 Fibonacci (iterative) ---")
print("First 10 Fibonacci numbers (iterative, F(0)=0, F(1)=1 based):")
# 为了与递归版本F(1)=1, F(2)=1 对齐，这里从1开始并期望得到相同序列
# 如果要严格按F(0)=0, F(1)=1, F(2)=1, F(3)=2... 那么迭代版本输出的就是第n项
# 这里我们调整一下，让迭代版本也输出 F(1)=1, F(2)=1...
def fibonacci_iterative_match_recursive(n):
    if n <= 0: raise ValueError("Input must be positive for this version")
    if n in (1,2): return 1
    a, b = 1, 1 # F(1)=1, F(2)=1
    for _ in range(n - 2): # 已经有前两项了
        a, b = b, a + b
    return b

for i_fib_iter in range(1, 11):
    print(f"F({i_fib_iter}) = {fibonacci_iterative_match_recursive(i_fib_iter)}")


# 2.4 斐波那契数列 (递归，使用 @lru_cache 优化)
# lru_cache 是一个装饰器，用于缓存函数调用的结果 (Memoization)
@lru_cache(maxsize=None) # maxsize=None 表示缓存无限制 (或使用默认128)
def fibonacci_recursive_optimized(n):
    """计算第n个斐波那契数 (递归，带LRU缓存优化) F(1)=1, F(2)=1"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("斐波那契数列的项数必须是正整数")
    if n in (1, 2):
        return 1
    return fibonacci_recursive_optimized(n - 1) + fibonacci_recursive_optimized(n - 2)

print("\n--- 2.2.3 Fibonacci (optimized recursive with @lru_cache) ---")
print("First 30 Fibonacci numbers (optimized):") # 可以计算更多项了
for i_fib_opt in range(1, 31):
    print(f"F({i_fib_opt}) = {fibonacci_recursive_optimized(i_fib_opt)}", end=" | ")
    if i_fib_opt % 5 == 0: print() # 每5个换行
print("\n")

print("--- End of Day 15 Advanced Functions Demo ---")