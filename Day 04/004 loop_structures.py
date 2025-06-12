# day_06_loop_structures.py

import time
import random

# -----------------------------------------------------------------------------
# 核心概念：循环结构 (Loop Structure)
# 控制某条或某些指令重复执行的结构。
# 类型：for-in 循环, while 循环
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、for-in 循环
# -----------------------------------------------------------------------------
# 推荐使用场景：明确知道循环执行的次数。
# 循环体：被 for-in 控制的缩进代码块。

# 1.1 使用 range() 控制循环次数
print("--- 1.1 for-in with range() ---")
# 每隔0.1秒输出一次“hello, world”，重复5次 (原文3600次太久)
# for i in range(5):
#     print(f'(Loop {i+1}) hello, world')
#     time.sleep(0.1)

# 1.2 range() 函数的用法
# - range(stop): [0, stop-1]
# - range(start, stop): [start, stop-1]
# - range(start, stop, step): [start, stop-1] with specified step
print("\n--- 1.2 range() examples ---")
print("range(5):")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print("\nrange(2, 6):")
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5
print("\nrange(1, 10, 2):")  # 奇数
for i in range(1, 10, 2):
    print(i, end=" ")  # 1 3 5 7 9
print("\nrange(10, 0, -2):")  # 递减偶数
for i in range(10, 0, -2):
    print(i, end=" ")  # 10 8 6 4 2

# 1.3 循环变量不使用时，惯用 '_'
print("\n\n--- 1.3 for-in with '_' as loop variable ---")
# for _ in range(3): # 示例中不实际休眠
#     print('Looping without using the loop variable.')
#     # time.sleep(0.1)

# 1.4 示例：从 1 到 100 的整数求和
print("\n--- 1.4 Sum of integers 1 to 100 (for-in) ---")
total_sum_for = 0
for i in range(1, 101):  # 1, 2, ..., 100
    total_sum_for += i
print(f"Sum (1-100) using for-in: {total_sum_for}")  # 5050

# 1.5 示例：从 1 到 100 的偶数求和 (方法1: if判断)
print("\n--- 1.5 Sum of even numbers 1 to 100 (for-in with if) ---")
total_even_sum_v1 = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even_sum_v1 += i
print(f"Sum of evens (1-100) using for-in and if: {total_even_sum_v1}")  # 2550

# 1.6 示例：从 1 到 100 的偶数求和 (方法2: range步长)
print("\n--- 1.6 Sum of even numbers 1 to 100 (for-in with range step) ---")
total_even_sum_v2 = 0
for i in range(2, 101, 2):  # 2, 4, ..., 100
    total_even_sum_v2 += i
print(f"Sum of evens (1-100) using for-in and range step: {total_even_sum_v2}")  # 2550

# 1.7 示例：从 1 到 100 的偶数求和 (方法3: sum函数)
print("\n--- 1.7 Sum of even numbers 1 to 100 (sum function) ---")
total_even_sum_v3 = sum(range(2, 101, 2))
print(f"Sum of evens (1-100) using sum(): {total_even_sum_v3}")  # 2550

# -----------------------------------------------------------------------------
# 二、while 循环
# -----------------------------------------------------------------------------
# 推荐使用场景：不能确定循环重复的次数，通过条件控制循环。
# 条件为 True 时执行循环体，为 False 时结束。

# 2.1 示例：从 1 到 100 的整数求和
print("\n--- 2.1 Sum of integers 1 to 100 (while) ---")
total_sum_while = 0
counter_while = 1
while counter_while <= 100:
    total_sum_while += counter_while
    counter_while += 1  # 必须更新循环控制变量
print(f"Sum (1-100) using while: {total_sum_while}")  # 5050

# 2.2 示例：从 1 到 100 的偶数求和
print("\n--- 2.2 Sum of even numbers 1 to 100 (while) ---")
total_even_sum_while = 0
even_counter_while = 2
while even_counter_while <= 100:
    total_even_sum_while += even_counter_while
    even_counter_while += 2
print(f"Sum of evens (1-100) using while: {total_even_sum_while}")  # 2550

# -----------------------------------------------------------------------------
# 三、break 和 continue
# -----------------------------------------------------------------------------
# break: 终止当前所在的循环结构。
# continue: 放弃本次循环后续代码，直接进入下一轮循环。

# 3.1 break 示例 (在 while True 循环中使用)
print("\n--- 3.1 break in while True loop ---")
# 从1到100的偶数求和 (使用 while True 和 break)
total_even_break = 0
i_break = 2
while True:  # "死循环"
    total_even_break += i_break
    i_break += 2
    if i_break > 100:
        break  # 当 i > 100 时跳出循环
print(f"Sum of evens (1-100) using while True and break: {total_even_break}")  # 2550

# 3.2 continue 示例
print("\n--- 3.2 continue in for loop ---")
# 从1到100的偶数求和 (使用 continue 跳过奇数)
total_even_continue = 0
for i_continue in range(1, 101):
    if i_continue % 2 != 0:  # 如果是奇数
        continue  # 跳过本次循环的后续语句 (total_even_continue += i_continue)
    total_even_continue += i_continue
print(f"Sum of evens (1-100) using for and continue: {total_even_continue}")  # 2550

# -----------------------------------------------------------------------------
# 四、嵌套的循环结构
# -----------------------------------------------------------------------------
# 循环结构内部可以包含其他循环结构。

# 4.1 示例：打印乘法口诀表 (九九表)
print("\n--- 4.1 Nested loops for multiplication table ---")
for i_outer in range(1, 10):  # 外层循环控制行 (1 to 9)
    for j_inner in range(1, i_outer + 1):  # 内层循环控制列 (1 to i_outer)
        print(f'{j_inner}×{i_outer}={i_outer * j_inner}', end='\t')  # 使用jxi更符合习惯
    print()  # 每行结束后换行

# -----------------------------------------------------------------------------
# 五、循环结构的应用
# -----------------------------------------------------------------------------

# 5.1 例子1：判断素数
# 素数：只能被 1 和自身整除的大于 1 的整数。
# 优化：检查因子到 sqrt(num) 即可。
print("\n--- 5.1 Prime number check ---")
num_to_check_prime = 29  # 假设输入
is_prime_flag = True
if num_to_check_prime <= 1:
    is_prime_flag = False
else:
    # 检查到 int(sqrt(num)) + 1 即可
    # 加1是为了确保range的右边界包含sqrt(num)本身（如果它是整数）
    limit_prime_check = int(num_to_check_prime ** 0.5) + 1
    for i_prime in range(2, limit_prime_check):
        if num_to_check_prime % i_prime == 0:
            is_prime_flag = False
            break  # 找到一个因子，即可确定不是素数，跳出循环

if is_prime_flag:
    print(f'{num_to_check_prime}是素数')
else:
    print(f'{num_to_check_prime}不是素数')

num_to_check_not_prime = 30
is_prime_flag_2 = True
if num_to_check_not_prime <= 1:
    is_prime_flag_2 = False
else:
    for i_prime in range(2, int(num_to_check_not_prime ** 0.5) + 1):
        if num_to_check_not_prime % i_prime == 0:
            is_prime_flag_2 = False;
            break
if is_prime_flag_2:
    print(f'{num_to_check_not_prime}是素数')
else:
    print(f'{num_to_check_not_prime}不是素数')

# 5.2 例子2：最大公约数 (GCD)
# 方法1: 从大到小遍历查找公因子
print("\n--- 5.2.1 GCD (brute force) ---")
x_gcd1 = 48  # 假设输入
y_gcd1 = 18  # 假设输入
# 确保x是较小的数，以减少循环次数（或者从min(x,y)开始）
if x_gcd1 > y_gcd1:
    x_gcd1, y_gcd1 = y_gcd1, x_gcd1  # 交换

gcd_val1 = 1  # 默认为1
for i_gcd1 in range(x_gcd1, 0, -1):  # 从较小的数开始递减
    if x_gcd1 % i_gcd1 == 0 and y_gcd1 % i_gcd1 == 0:
        gcd_val1 = i_gcd1
        break
print(f'GCD of {x_gcd1} and {y_gcd1} (brute force): {gcd_val1}')

# 方法2: 欧几里得算法 (辗转相除法)
print("\n--- 5.2.2 GCD (Euclidean algorithm) ---")
x_gcd2 = 48  # 假设输入
y_gcd2 = 18  # 假设输入
# 确保 x_gcd2 是被除数，y_gcd2 是除数，且 x_gcd2 > y_gcd2 (习惯上)
# 实际算法中，初始大小顺序不影响最终结果，但为了演示，可以先排序
a_euclid = max(x_gcd2, y_gcd2)
b_euclid = min(x_gcd2, y_gcd2)

while b_euclid != 0:  # 或者 while a_euclid % b_euclid != 0 (原文是 y % x != 0)
    a_euclid, b_euclid = b_euclid, a_euclid % b_euclid
gcd_val2 = a_euclid  # 当 b_euclid 为 0 时，a_euclid 就是最大公约数
print(f'GCD of {x_gcd2} and {y_gcd2} (Euclidean): {gcd_val2}')

# 原文欧几里得算法的写法:
# x_orig_euclid = 18 # 假设输入（对应原文的x）
# y_orig_euclid = 48 # 假设输入（对应原文的y）
# # 这种写法下，x最终会变成GCD
# # while y_orig_euclid % x_orig_euclid != 0:
# #     x_orig_euclid, y_orig_euclid = y_orig_euclid % x_orig_euclid, x_orig_euclid
# # print(f'GCD (original Euclidean logic): {x_orig_euclid}')
# # 为了避免混淆，我们使用更标准的 a, b
a_std, b_std = 48, 18
while b_std:  # while b_std != 0
    a_std, b_std = b_std, a_std % b_std
print(f'GCD of 48 and 18 (standard Euclidean): {a_std}')

# 5.3 例子3：猜数字游戏
print("\n--- 5.3 Guess the number game ---")
# answer_game = random.randrange(1, 101) # 1 到 100 的随机整数
# counter_game = 0
# print("Guess a number between 1 and 100.")
# while True:
#     counter_game += 1
#     try:
#         # num_guess = int(input(f'Attempt {counter_game}, enter your guess: ')) # 实际游戏中会用input
#         if counter_game == 1: num_guess = 50 # 模拟第一次猜
#         elif counter_game == 2: num_guess = 75 # 模拟第二次猜
#         elif counter_game == 3: num_guess = answer_game # 模拟第三次猜对
#         else: num_guess = answer_game # 确保能结束

#         print(f"You guessed: {num_guess}")
#         if num_guess < answer_game:
#             print('Too small, try a bigger number.')
#         elif num_guess > answer_game:
#             print('Too big, try a smaller number.')
#         else:
#             print('Congratulations! You guessed it.')
#             break
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
# print(f'You guessed the number in {counter_game} attempts.')
# 简化的演示，不进行实际输入
answer_demo = 42
counter_demo = 0
guesses_demo = [30, 50, 40, 42]  # 模拟猜测序列
print(f"(The secret number is {answer_demo})")
for guess in guesses_demo:
    counter_demo += 1
    print(f"Attempt {counter_demo}: You guess {guess}")
    if guess < answer_demo:
        print("Too small.")
    elif guess > answer_demo:
        print("Too big.")
    else:
        print("Correct!")
        break
print(f"Finished in {counter_demo} attempts.")

print("\n--- End of Day 06 Loop Structures Demo ---")