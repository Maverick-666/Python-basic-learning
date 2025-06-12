# day_15_function_applications.py

import random
import string
import math # 虽然原文例子没直接用，但计算方差标准差等可能会用到

# -----------------------------------------------------------------------------
# 核心：通过实际案例巩固函数定义、参数、返回值、模块导入等。
# 强调将独立且重复使用的功能封装成函数。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 例子1：随机验证码
# 验证码由数字和英文大小写字母构成，长度可设置。
# -----------------------------------------------------------------------------
print("--- 例子1：随机验证码 ---")
ALL_CHARS_EX1 = string.digits + string.ascii_letters # '0123...xyz...XYZ'

def generate_code_ex1(*, code_len=4):
    """
    生成指定长度的验证码。
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    # random.choices 实现有放回抽样
    # 参数 k 是命名关键字参数
    return ''.join(random.choices(ALL_CHARS_EX1, k=code_len))

print("生成5组默认长度(4)的验证码:")
for _ in range(5):
    print(generate_code_ex1())

print("\n生成5组长度为6的验证码:")
for _ in range(5):
    print(generate_code_ex1(code_len=6))
print("\n")

# -----------------------------------------------------------------------------
# 例子2：判断素数
# 质数是只能被1和自身整除的正整数（大于1）。
# -----------------------------------------------------------------------------
print("--- 例子2：判断素数 ---")
def is_prime_ex2(num: int) -> bool:
    """
    判断一个正整数是不是质数。
    :param num: 大于1的正整数
    :return: 如果num是质数返回True，否则返回False
    """
    if num <= 1: # 确保输入大于1，虽然题目说参数是大于1的正整数
        return False
    # 优化：检查因子到 sqrt(num) 即可
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False # 找到因子，不是素数
    return True # 没有找到因子 (除了1和自身)

print(f"Is 2 prime? {is_prime_ex2(2)}")   # True
print(f"Is 3 prime? {is_prime_ex2(3)}")   # True
print(f"Is 4 prime? {is_prime_ex2(4)}")   # False
print(f"Is 17 prime? {is_prime_ex2(17)}") # True
print(f"Is 25 prime? {is_prime_ex2(25)}") # False
print(f"Is 97 prime? {is_prime_ex2(97)}") # True
print("\n")

# -----------------------------------------------------------------------------
# 例子3：最大公约数 (GCD) 和最小公倍数 (LCM)
# -----------------------------------------------------------------------------
print("--- 例子3：最大公约数和最小公倍数 ---")

def gcd_ex3(x: int, y: int) -> int:
    """求最大公约数 (欧几里得算法)"""
    # 确保x是较大的数，或者算法本身能处理顺序
    # while y % x != 0: # 原文逻辑，假设x是较小的那个，并最终成为GCD
    #     x, y = y % x, x
    # return x
    # 更通用的欧几里得算法
    while y: # 当y不为0时
        x, y = y, x % y
    return abs(x) # 返回绝对值确保是正整数，以防输入负数

def lcm_ex3(x: int, y: int) -> int:
    """求最小公倍数，公式: (x * y) // gcd(x, y)"""
    if x == 0 or y == 0: # LCM of 0 and anything is 0
        return 0
    return abs(x * y) // gcd_ex3(x, y) # 使用abs确保结果为正

num1_ex3, num2_ex3 = 12, 18
print(f"GCD of {num1_ex3} and {num2_ex3}: {gcd_ex3(num1_ex3, num2_ex3)}") # 6
print(f"LCM of {num1_ex3} and {num2_ex3}: {lcm_ex3(num1_ex3, num2_ex3)}") # 36

num3_ex3, num4_ex3 = 7, 5
print(f"GCD of {num3_ex3} and {num4_ex3}: {gcd_ex3(num3_ex3, num4_ex3)}") # 1 (互质)
print(f"LCM of {num3_ex3} and {num4_ex3}: {lcm_ex3(num3_ex3, num4_ex3)}") # 35
print("\n")

# -----------------------------------------------------------------------------
# 例子4：数据统计
# 算术平均值、中位数、极差、方差、标准差、变异系数
# -----------------------------------------------------------------------------
print("--- 例子4：数据统计 ---")

def mean_ex4(data: list) -> float:
    """算术平均"""
    if not data: return 0.0 # 处理空列表
    return sum(data) / len(data)

def median_ex4(data: list) -> float:
    """中位数"""
    if not data: return 0.0
    temp_sorted, size = sorted(data), len(data)
    if size % 2 != 0: # 奇数个
        return float(temp_sorted[size // 2])
    else: # 偶数个
        mid1 = temp_sorted[size // 2 - 1]
        mid2 = temp_sorted[size // 2]
        return (mid1 + mid2) / 2.0

def ptp_ex4(data: list) -> float: # Peak to Peak (Range)
    """极差（全距）"""
    if not data: return 0.0
    return float(max(data) - min(data))

def var_ex4(data: list, ddof=1) -> float: # ddof: Delta Degrees of Freedom
    """方差 (ddof=1 for sample variance, ddof=0 for population variance)"""
    if len(data) <= ddof: return 0.0 # 避免除以0或负数
    x_bar = mean_ex4(data)
    # temp_sum_sq_diff = sum([(num - x_bar) ** 2 for num in data]) # 列表生成式
    # 更高效的写法，避免创建中间列表
    temp_sum_sq_diff = 0
    for num in data:
        temp_sum_sq_diff += (num - x_bar) ** 2
    return temp_sum_sq_diff / (len(data) - ddof)

def std_ex4(data: list, ddof=1) -> float:
    """标准差"""
    return var_ex4(data, ddof) ** 0.5

def cv_ex4(data: list, ddof=1) -> float:
    """变异系数"""
    data_mean = mean_ex4(data)
    if data_mean == 0: return float('inf') # 或者根据情况返回NaN或0
    return std_ex4(data, ddof) / data_mean

def describe_ex4(data: list, sample_ddof=1):
    """输出描述性统计信息"""
    if not data:
        print("Data list is empty. Cannot compute statistics.")
        return
    print(f'样本数量: {len(data)}')
    print(f'均值: {mean_ex4(data):.2f}')
    print(f'中位数: {median_ex4(data):.2f}')
    print(f'极差: {ptp_ex4(data):.2f}')
    print(f'方差 (ddof={sample_ddof}): {var_ex4(data, ddof=sample_ddof):.2f}')
    print(f'标准差 (ddof={sample_ddof}): {std_ex4(data, ddof=sample_ddof):.2f}')
    print(f'变异系数 (ddof={sample_ddof}): {cv_ex4(data, ddof=sample_ddof):.2%}') # 输出为百分比

sample_data_ex4 = [10, 12, 15, 11, 13, 14, 12, 16, 10, 13, 14, 15]
print("描述性统计信息 for sample_data_ex4:")
describe_ex4(sample_data_ex4)
print("\n")

# -----------------------------------------------------------------------------
# 例子5：双色球随机选号 (函数重构)
# -----------------------------------------------------------------------------
print("--- 例子5：双色球随机选号 (函数重构) ---")

RED_BALLS_POOL_EX5 = list(range(1, 34)) # 1 to 33
BLUE_BALLS_POOL_EX5 = list(range(1, 17)) # 1 to 16

def choose_balls_ex5() -> list:
    """生成一组随机号码 (6红+1蓝)"""
    selected_reds = random.sample(RED_BALLS_POOL_EX5, 6) # 无放回抽样6个红球
    selected_reds.sort()
    blue_ball = random.choice(BLUE_BALLS_POOL_EX5) # 随机选1个蓝球
    selected_reds.append(blue_ball) # 将蓝球加到列表末尾
    return selected_reds

def display_balls_ex5(balls: list):
    """格式输出一组号码 (前6个红球，最后1个蓝球)"""
    # 原文使用颜色控制码，这里简化为普通打印
    red_to_print = balls[:-1]
    blue_to_print = balls[-1]
    print("红球:", " ".join([f"{ball:0>2d}" for ball in red_to_print]), end=" ")
    print(f"蓝球: [{blue_to_print:0>2d}]")

# num_sets_ex5 = int(input('生成几注号码: ')) # 原文方式
num_sets_ex5 = 3 # 固定生成3注用于演示
print(f"生成 {num_sets_ex5} 注双色球号码:")
for _ in range(num_sets_ex5):
    chosen_set = choose_balls_ex5()
    display_balls_ex5(chosen_set)
print("\n")

print("--- End of Day 15 Function Applications Demo ---")