# iterators_and_generators.py

import sys

# -----------------------------------------------------------------------------
# 一、迭代器 (Iterator)
# - 迭代是访问集合元素的一种方式。
# - 迭代器是一个可以记住遍历位置的对象。
# - 从集合的第一个元素开始访问，直到所有元素被访问完结束。
# - 只能往前不会后退。
# - 核心方法：iter() 和 next()。
# -----------------------------------------------------------------------------
print("--- 1. 迭代器 ---")

# 1.1 从可迭代对象 (如列表、元组、字符串) 创建迭代器
print("--- 1.1 创建和使用迭代器 ---")
my_list_iter = [1, 2, 3, 4]
it_list = iter(my_list_iter) # 创建迭代器对象

print(f"Next element from list iterator: {next(it_list)}") # 1
print(f"Next element from list iterator: {next(it_list)}") # 2

# 1.2 使用 for 循环遍历迭代器
# for 循环会自动调用 iter() 获取迭代器，并处理 StopIteration 异常
print("\nUsing for loop with the rest of list iterator:")
for x_list_iter in it_list: # it_list 会从上次 next() 的位置继续
    print(x_list_iter, end=" ") # 3 4
print("\n")

# 1.3 使用 while True 和 next() 模拟 for 循环遍历
print("Simulating for loop with while True and next():")
my_tuple_iter = ('a', 'b', 'c')
it_tuple = iter(my_tuple_iter)
while True:
    try:
        element = next(it_tuple)
        print(element)
    except StopIteration: # 当没有更多元素时，next() 引发 StopIteration
        # sys.exit() # 在脚本中通常用break或return代替sys.exit()
        break
print("\n")

# 1.4 创建一个自定义迭代器类
# 需要实现 __iter__() 和 __next__() 方法。
# __iter__() 返回迭代器对象自身 (self)。
# __next__() 返回下一个值，并在没有更多值时引发 StopIteration。

print("--- 1.4 自定义迭代器类 (MyNumbers) ---")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self # 返回迭代器对象自身

    def __next__(self):
        if self.a <= 5: # 迭代5次后停止 (示例)
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # 标识迭代完成

my_class_instance = MyNumbers()
my_iter_from_class = iter(my_class_instance) # 调用 my_class_instance.__iter__()

print(f"Custom iterator next: {next(my_iter_from_class)}") # 1
print(f"Custom iterator next: {next(my_iter_from_class)}") # 2

print("\nLooping through custom iterator:")
# for num_from_class in my_class_instance: # 也可以直接用实例，因为它实现了__iter__
# 注意：如果上面已经用next()消耗了一部分，这里会从消耗后的位置开始
# 为清晰起见，我们重新创建一个实例
my_class_instance_for_loop = MyNumbers()
for num_from_class in my_class_instance_for_loop:
    print(num_from_class, end=" ") # 1 2 3 4 5
print("\n")

# 1.5 StopIteration 示例
# (已在 MyNumbers 类中演示)
# 另一个示例：迭代20次后停止
class LimitedNumbers:
    def __iter__(self):
        self.current = 1
        return self
    def __next__(self):
        if self.current <= 3: # 原文20，改为3便于演示
            x = self.current
            self.current += 1
            return x
        else:
            raise StopIteration

print("LimitedNumbers iterator (stops after 3 iterations):")
limited_iter_instance = LimitedNumbers()
for val_limited in limited_iter_instance:
    print(val_limited)
print("\n")


# -----------------------------------------------------------------------------
# 二、生成器 (Generator)
# - 使用了 yield 关键字的函数被称为生成器函数。
# - yield 用于在迭代过程中逐步产生值，而不是一次性返回所有结果。
# - 调用生成器函数返回一个生成器对象 (也是一种迭代器)。
# - 函数执行到 yield 时暂停，返回值，并在下次调用 next() 时从暂停处继续。
# - 优点：按需生成值，节省内存，代码简洁。
# -----------------------------------------------------------------------------
print("--- 2. 生成器 ---")

# 2.1 简单的生成器函数示例 (countdown)
print("--- 2.1 countdown 生成器 ---")
def countdown_generator(n):
    print("Countdown started (generator function execution starts)")
    while n > 0:
        print(f"Yielding {n}...")
        yield n # 暂停并返回值
        print(f"Resumed after yielding {n}")
        n -= 1
    print("Countdown finished (generator function execution ends)")

# 创建生成器对象
gen_countdown = countdown_generator(3) # 注意：此时函数体内的代码还未执行
print(f"Type of gen_countdown: {type(gen_countdown)}")

# 通过 next() 获取值
print(f"First next(gen_countdown): {next(gen_countdown)}") # 输出: 3


# 使用 for 循环迭代剩余的值
print("\nUsing for loop for the rest of gen_countdown:")
for value_countdown in gen_countdown: # 会从上次暂停的地方继续
    print(f"For loop got: {value_countdown}") # 输出: 1
print("\n")

# 2.2 使用 yield 实现斐波那契数列生成器
print("--- 2.2 Fibonacci 生成器 ---")
def fibonacci_generator(max_count): # 生成指定数量的斐波那契数
    a, b, counter = 0, 1, 0
    while counter < max_count: # 原文是 counter > n 然后 return，这里改为生成指定数量
        yield a
        a, b = b, a + b
        counter += 1

# f_fib_gen 是一个迭代器 (生成器对象)
f_fib_gen = fibonacci_generator(10) # 生成前10个斐波那契数 (0-indexed)

print("Fibonacci sequence (first 10 numbers using generator):")
# 使用 for 循环遍历生成器
for num_fib in f_fib_gen:
    print(num_fib, end=" ") # 0 1 1 2 3 5 8 13 21 34
print("\n")

# 另一种遍历生成器的方式 (原文的while True + try/except)
print("\nFibonacci sequence (using while True, next(), try/except):")
f_fib_gen_alt = fibonacci_generator(5)
while True:
     try:
         print(next(f_fib_gen_alt), end=" ")
     except StopIteration:
         # sys.exit() # 在脚本中通常用break
         break
print("\n")


# -----------------------------------------------------------------------------
# 生成器表达式 (Generator Expressions) - (本单元未直接讲解，但与生成器密切相关)
# - 类似于列表生成式，但使用圆括号 ()。
# - 创建一个生成器对象，按需生成值，而不是立即创建一个列表。
# - 语法：(expression for item in iterable if condition)
# -----------------------------------------------------------------------------
print("--- (Bonus) 生成器表达式 ---")
gen_expr = (x * x for x in range(5)) # 创建生成器对象
print(f"Type of gen_expr: {type(gen_expr)}")

print("Values from generator expression:")
for val_expr in gen_expr:
    print(val_expr, end=" ") # 0 1 4 9 16
print("\n")

print("--- End of Iterators and Generators Demo ---")



print("还没有结束")
def sub_generator():
    yield "Sub 1"
    yield "Sub 2"


def main_generator_manual():
    yield "Main Start"
    for item in sub_generator():  # 手动迭代子生成器
        yield item
    yield "Main End"


def main_generator_yield_from():
    yield "Main Start (yield from)"
    yield from sub_generator()  # 使用 yield from
    yield "Main End (yield from)"


print("\n--- Manual Sub-iteration ---")
for item in main_generator_manual():
    print(item)

print("\n--- Using yield from ---")
for item in main_generator_yield_from():
    print(item)