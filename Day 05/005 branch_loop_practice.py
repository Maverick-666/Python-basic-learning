# day_07_branch_loop_practice.py

import random

# -----------------------------------------------------------------------------
# 核心：通过实战案例巩固分支结构和循环结构的应用。
# 强调练习量对于掌握编程的重要性。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 例子1：100以内的素数
# 素数：只能被 1 和自身整除的正整数（不包括 1）。
# -----------------------------------------------------------------------------
print("--- 例子1：100以内的素数 ---")
for num_prime_candidate in range(2, 100): # 遍历 2 到 99
    is_prime_flag_ex1 = True
    # 优化：检查因子到 sqrt(num) 即可
    for i_factor_check in range(2, int(num_prime_candidate ** 0.5) + 1):
        if num_prime_candidate % i_factor_check == 0:
            is_prime_flag_ex1 = False
            break # 找到一个因子，即可确定不是素数
    if is_prime_flag_ex1:
        print(num_prime_candidate, end=" ")
print("\n")

# -----------------------------------------------------------------------------
# 例子2：斐波那契数列
# 前两个数是1 (或0,1)，从第三个数开始，每个数都是它前面两个数的和。
# 序列: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... (如果从0,1开始)
# 原文从 a,b = 0,1 开始，打印的是 b 的后续值，即 1, 1, 2, 3...
# -----------------------------------------------------------------------------
print("--- 例子2：斐波那契数列 (前20个数) ---")
a_fib, b_fib = 0, 1 # a_fib 代表 F(n-2), b_fib 代表 F(n-1)
fib_sequence = []
for _ in range(20):
    # 原文逻辑：先更新a,b，然后打印更新后的a (即原来的b)
    # a_fib, b_fib = b_fib, a_fib + b_fib
    # print(a_fib, end=" ")
    # 为了更清晰地展示序列，我们先打印当前项，再更新
    # 如果序列定义为 F(0)=0, F(1)=1，则打印 b 即可 (或 a，取决于如何初始化)
    # 若按原文先打印a，且a,b = 0,1, 则第一项是更新后的a, 即原来的b=1
    # 我们这里直接打印 b 作为当前项，然后计算下一项
    # print(b_fib, end=" ") # 如果从 F(1)=1, F(2)=1 开始，初始化 a=1, b=1，打印a
    # 按原文输出逻辑: 0,1 -> b, a+b -> 1, 1 -> print(1)
    #                1,1 -> b, a+b -> 1, 2 -> print(1)
    #                1,2 -> b, a+b -> 2, 3 -> print(2)
    # 这样打印的是 F(1), F(2), F(3)...
    a_fib, b_fib = b_fib, a_fib + b_fib # a_fib 现在是 F(n), b_fib 是 F(n+1)
    fib_sequence.append(a_fib)          # 将 F(n) 添加到列表

print(" ".join(map(str, fib_sequence))) # 输出: 1 1 2 3 5 8 ...
print("\n")

# -----------------------------------------------------------------------------
# 例子3：寻找水仙花数 (100到999)
# 水仙花数：一个N位非负整数，其各位数字的N次方和等于该数本身。
# 例如: 153 = 1^3 + 5^3 + 3^3
# -----------------------------------------------------------------------------
print("--- 例子3：寻找水仙花数 (100-999) ---")
narcissistic_numbers = []
for num_narcissistic in range(100, 1000):
    # 拆分三位数
    low_digit = num_narcissistic % 10        # 个位
    mid_digit = (num_narcissistic // 10) % 10 # 十位
    high_digit = num_narcissistic // 100      # 百位

    if num_narcissistic == (low_digit ** 3 + mid_digit ** 3 + high_digit ** 3):
        narcissistic_numbers.append(num_narcissistic)
print("100到999之间的水仙花数:", " ".join(map(str, narcissistic_numbers))) # 153 370 371 407
print("\n")

# 3.1 附：正整数的反转
print("--- 附：正整数的反转 ---")
num_to_reverse = 12389 # 假设输入
original_num_for_print = num_to_reverse
reversed_num_result = 0
while num_to_reverse > 0:
    digit = num_to_reverse % 10
    reversed_num_result = reversed_num_result * 10 + digit
    num_to_reverse //= 10 # 整数除法，去掉最后一位
print(f"原始数字: {original_num_for_print}, 反转后: {reversed_num_result}") # 98321
print("\n")

# -----------------------------------------------------------------------------
# 例子4：百钱百鸡问题
# 公鸡5元/只, 母鸡3元/只, 小鸡1元/3只。100元买100只鸡。
# x: 公鸡数量, y: 母鸡数量, z: 小鸡数量
# 条件1: x + y + z = 100 (数量)
# 条件2: 5*x + 3*y + z/3 = 100 (钱数)
# 且 z 必须是 3 的倍数。
# -----------------------------------------------------------------------------
print("--- 例子4：百钱百鸡问题 ---")
print("方法一 (三层嵌套，原文版本):")
solutions_v1 = []
for x_rooster_v1 in range(0, 21):      # 公鸡最多买 100/5 = 20 只
    for y_hen_v1 in range(0, 34):      # 母鸡最多买 100/3 approx 33 只
        for z_chick_v1 in range(0, 101, 3): # 小鸡数量是3的倍数，最多100只
            if (x_rooster_v1 + y_hen_v1 + z_chick_v1 == 100 and
                    5 * x_rooster_v1 + 3 * y_hen_v1 + z_chick_v1 // 3 == 100):
                solutions_v1.append(f'公鸡: {x_rooster_v1}, 母鸡: {y_hen_v1}, 小鸡: {z_chick_v1}')
for sol in solutions_v1: print(sol)

print("\n方法二 (两层嵌套，优化版):")
solutions_v2 = []
for x_rooster_v2 in range(0, 21):
    for y_hen_v2 in range(0, 34):
        z_chick_v2 = 100 - x_rooster_v2 - y_hen_v2
        # 检查 z 是否为非负数且是3的倍数
        if z_chick_v2 >= 0 and z_chick_v2 % 3 == 0:
            if 5 * x_rooster_v2 + 3 * y_hen_v2 + z_chick_v2 // 3 == 100:
                solutions_v2.append(f'公鸡: {x_rooster_v2}, 母鸡: {y_hen_v2}, 小鸡: {z_chick_v2}')
for sol in solutions_v2: print(sol)
# 可能的解:
# 公鸡: 0, 母鸡: 25, 小鸡: 75
# 公鸡: 4, 母鸡: 18, 小鸡: 78
# 公鸡: 8, 母鸡: 11, 小鸡: 81
# 公鸡: 12, 母鸡: 4, 小鸡: 84
print("\n")

# -----------------------------------------------------------------------------
# 例子5：CRAPS赌博游戏 (简化版演示，不进行实际输入)
# 规则：
# 1. 首次摇骰子 (两颗):
#    - 7 或 11点: 玩家胜
#    - 2, 3 或 12点: 庄家胜 (玩家输)
#    - 其他点数 (4,5,6,8,9,10): 记为 "目标点数", 游戏继续
# 2. 继续摇骰子:
#    - 摇出 7点: 庄家胜 (玩家输)
#    - 摇出 "目标点数": 玩家胜
#    - 其他点数: 继续摇
# 玩家初始资金1000，每局下注。输光则游戏结束。
# -----------------------------------------------------------------------------
print("--- 例子5：CRAPS赌博游戏 (模拟运行) ---")
initial_money_craps = 100 # 初始资金 (原文1000，改为100便于快速结束)
current_money_craps = initial_money_craps
game_round = 0

# 模拟几局游戏，不进行真实下注输入
simulated_bets_rolls = [
    (10, [(3,4), (2,2)]),          # 第一次7点，玩家胜 (10+10=20) -> money=110
    (20, [(1,1)]),                # 第一次2点，庄家胜 (20) -> money=90
    (15, [(2,3), (3,3), (4,3)]),  # 第一次5点(目标), 第二次6点, 第三次7点(目标前出7)，庄家胜 (15) -> money=75
    (25, [(4,2), (1,2), (3,3)]),  # 第一次6点(目标), 第二次3点, 第三次6点(摇出目标)，玩家胜 (25+25=50) -> money=100
    (100, [(6,6)]),               # 第一次12点，庄家胜 (100) -> money=0, 破产
    (10, [(1,2)])                 # 如果上面没破产，这一局不会执行
]

print(f"初始资金: {current_money_craps}元")

for debt_amount, rolls_sequence in simulated_bets_rolls:
    game_round += 1
    if current_money_craps <= 0:
        print("\n已破产，无法继续游戏。")
        break

    print(f"\n--- 第 {game_round} 局 ---")
    print(f'当前总资产: {current_money_craps}元')

    if not (0 < debt_amount <= current_money_craps):
        print(f"模拟下注金额 {debt_amount} 无效或超出资产，跳过此局。")
        continue
    print(f'玩家下注: {debt_amount}元')

    # 第一次摇骰子
    first_roll_dice1, first_roll_dice2 = rolls_sequence[0]
    first_point_craps = first_roll_dice1 + first_roll_dice2
    print(f'玩家第一次摇出了 {first_roll_dice1} + {first_roll_dice2} = {first_point_craps}点')

    if first_point_craps == 7 or first_point_craps == 11:
        print('玩家胜!')
        current_money_craps += debt_amount
    elif first_point_craps == 2 or first_point_craps == 3 or first_point_craps == 12:
        print('庄家胜!')
        current_money_craps -= debt_amount
    else:
        print(f'目标点数: {first_point_craps}')
        # 继续摇骰子
        target_point_craps = first_point_craps
        for i in range(1, len(rolls_sequence)): # 从第二次摇骰子开始
            current_roll_dice1, current_roll_dice2 = rolls_sequence[i]
            current_point_craps = current_roll_dice1 + current_roll_dice2
            print(f'玩家接着摇出了 {current_roll_dice1} + {current_roll_dice2} = {current_point_craps}点')
            if current_point_craps == 7:
                print('庄家胜!')
                current_money_craps -= debt_amount
                break # 当前这局结束
            elif current_point_craps == target_point_craps:
                print('玩家胜!')
                current_money_craps += debt_amount
                break # 当前这局结束
        else: # for 循环正常结束 (没有通过 break 跳出)
            if current_point_craps != 7 and current_point_craps != target_point_craps:
                 print("模拟的摇骰子序列结束，但未分胜负（通常游戏会继续）。")


if current_money_craps <= 0:
    print('\n你破产了, 游戏结束!')
else:
    print(f'\n游戏模拟结束，剩余资产: {current_money_craps}元')

print("\n--- End of Day 07 Branch and Loop Practice Demo ---")