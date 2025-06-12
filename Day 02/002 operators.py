# day_04_operators.py

# -----------------------------------------------------------------------------
# 核心概念：表达式 (Expression)
# 表达式是计算机程序中的句法实体，它由一个或多个常量、变量、函数和运算符组合而成，
# 编程语言可以对其进行解释和计算以得到另一个值。
# 运算符优先级：决定了在一个表达式中多个运算符的执行顺序。
# 可以使用圆括号 () 来改变或明确运算顺序。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、算术运算符 (Arithmetic Operators)
# -----------------------------------------------------------------------------
# 包括：+ (加), - (减), * (乘), / (除), // (整除), % (模/取余), ** (幂)

# 1.1 基本算术运算
print("--- 1.1 Basic Arithmetic ---")
num1 = 321
num2 = 12
print(f"{num1} + {num2} = {num1 + num2}")     # 加法运算，输出333
print(f"{num1} - {num2} = {num1 - num2}")     # 减法运算，输出309
print(f"{num1} * {num2} = {num1 * num2}")     # 乘法运算，输出3852
print(f"{num1} / {num2} = {num1 / num2}")     # 除法运算，输出26.75 (结果总是float)
print(f"{num1} // {num2} = {num1 // num2}")   # 整除运算，输出26 (结果取整数部分)
print(f"{num1} % {num2} = {num1 % num2}")     # 求模运算，输出9 (余数)
print(f"{num1} ** {num2} = {num1 ** num2}")   # 求幂运算

# 1.2 算术运算的优先级
# 优先级：** (最高) -> *, /, //, % -> +, - (最低)
# 使用 () 控制优先级
print("\n--- 1.2 Arithmetic Precedence ---")
print(f"2 + 3 * 5 = {2 + 3 * 5}")                  # 17 (先乘后加)
print(f"(2 + 3) * 5 = {(2 + 3) * 5}")              # 25 (括号优先)
print(f"(2 + 3) * 5 ** 2 = {(2 + 3) * 5 ** 2}")    # 125 (先幂，再括号内加，最后乘)
# 5**2 = 25; (2+3)=5; 5*25 = 125
print(f"((2 + 3) * 5) ** 2 = {((2 + 3) * 5) ** 2}") # 625 (内层括号，然后乘，最后幂)
# (2+3)=5; 5*5=25; 25**2 = 625

# -----------------------------------------------------------------------------
# 二、赋值运算符 (Assignment Operators)
# -----------------------------------------------------------------------------
# 基本赋值：=
# 复合赋值：+=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

# 2.1 基本赋值与复合赋值
print("\n--- 2.1 Assignment and Compound Assignment ---")
a = 10
b = 3
print(f"Initial a = {a}, b = {b}")

a_plus_equal_b = a  # 创建副本用于演示
a_plus_equal_b += b  # 相当于: a_plus_equal_b = a_plus_equal_b + b
print(f"a += b (where a={a}, b={b}): result = {a_plus_equal_b}") # 13

# 原文示例:
# a = 10 (b=3)
# a += b  => a becomes 10 + 3 = 13
# a *= a + 2 => a becomes 13 * (13 + 2) = 13 * 15 = 195
original_a = 10
original_b = 3
original_a += original_b
original_a *= original_a + 2
print(f"Original example: a=10, b=3; a += b; a *= a + 2; final a = {original_a}") # 195

# 2.2 海象运算符 (Walrus Operator) := (Python 3.8+)
# 作用：在表达式内部为变量赋值，并且表达式本身的值是赋给变量的值。
print("\n--- 2.2 Walrus Operator ---")
# print((x = 10)) # SyntaxError: invalid syntax (赋值语句不是表达式)
# print(x = 10)   # TypeError: 'x' is an invalid keyword argument for print()

if (n := len("hello world")) > 5: # 在判断条件中赋值
    print(f"The string has {n} characters, which is greater than 5.")
else:
    print(f"The string has {n} characters.")

# 原文示例
print(f"Value of (walrus_var := 10) is: {(walrus_var := 10)}") # 输出 10
print(f"Value of walrus_var after expression: {walrus_var}")      # 输出 10

# -----------------------------------------------------------------------------
# 三、比较运算符 (Comparison/Relational Operators)
# -----------------------------------------------------------------------------
# 包括：== (等于), != (不等于), > (大于), < (小于), >= (大于等于), <= (小于等于)
# 结果是布尔值：True 或 False

print("\n--- 3. Comparison Operators ---")
val1 = 10
val2 = 5
val3 = 10

print(f"{val1} == {val2}: {val1 == val2}")  # False
print(f"{val1} == {val3}: {val1 == val3}")  # True
print(f"{val1} != {val2}: {val1 != val2}")  # True
print(f"{val1} > {val2}: {val1 > val2}")    # True
print(f"{val1} < {val2}: {val1 < val2}")    # False
print(f"{val1} >= {val3}: {val1 >= val3}")  # True
print(f"{val2} <= {val1}: {val2 <= val1}")  # True

# -----------------------------------------------------------------------------
# 四、逻辑运算符 (Logical Operators)
# -----------------------------------------------------------------------------
# 包括：and (逻辑与), or (逻辑或), not (逻辑非)
# 用于组合或反转布尔表达式。
# 具有短路特性：
# - `x and y`: 如果 x 为 False，则不计算 y。
# - `x or y`: 如果 x 为 True，则不计算 y。

print("\n--- 4. Logical Operators ---")
flag_true = True
flag_false = False

print(f"{flag_true} and {flag_false}: {flag_true and flag_false}")  # False
print(f"{flag_true} and {flag_true}: {flag_true and flag_true}")    # True
print(f"{flag_false} and {flag_false}: {flag_false and flag_false}")# False

print(f"{flag_true} or {flag_false}: {flag_true or flag_false}")    # True
print(f"{flag_true} or {flag_true}: {flag_true or flag_true}")      # True
print(f"{flag_false} or {flag_false}: {flag_false or flag_false}")  # False

print(f"not {flag_true}: {not flag_true}")    # False
print(f"not {flag_false}: {not flag_false}")  # True

# 原文示例
flag0 = (1 == 1) # True
flag1 = (3 > 2)  # True
flag2 = (2 < 1)  # False
flag3 = flag1 and flag2 # True and False -> False
flag4 = flag1 or flag2  # True or False -> True
flag5 = not flag0       # not True -> False
print(f"flag0 (1==1) = {flag0}")
print(f"flag1 (3>2) = {flag1}")
print(f"flag2 (2<1) = {flag2}")
print(f"flag3 (flag1 and flag2) = {flag3}")
print(f"flag4 (flag1 or flag2) = {flag4}")
print(f"flag5 (not flag0) = {flag5}")
print(f"flag1 and not flag2: {flag1 and not flag2}") # True and not False -> True and True -> True
print(f"1 > 2 or 2 == 3: {(1 > 2) or (2 == 3)}")    # False or False -> False

# -----------------------------------------------------------------------------
# 五、运算符应用示例
# -----------------------------------------------------------------------------

# 5.1 华氏温度转摄氏温度 C = (F - 32) / 1.8
print("\n--- 5.1 Fahrenheit to Celsius ---")
# f_temp_str = input("请输入华氏温度 (e.g., 68): ") # 示例中不实际运行input，直接赋值
f_temp = 68.0 # 假设输入
c_temp = (f_temp - 32) / 1.8
# 使用 % 格式化 (旧式)
print('%.1f华氏度 = %.1f摄氏度' % (f_temp, c_temp))
# 使用 f-string (推荐)
print(f'{f_temp:.1f}华氏度 = {c_temp:.1f}摄氏度')

# 5.2 计算圆的周长和面积 (周长 = 2πr, 面积 = πr²)
print("\n--- 5.2 Circle Perimeter and Area ---")
import math # 导入math模块以使用 math.pi

radius_str = "5.5" # 假设输入
radius = float(radius_str)
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2 # 或 math.pi * radius * radius

# 使用 % 格式化
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
# 使用 f-string
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')
# 使用 f-string (Python 3.8+，带变量名)
print(f'{perimeter = :.2f}')
print(f'{area = :.2f}')

# 5.3 判断闰年 (Gregorian calendar rules after 1582)
# 1. 公元年份非 4 的倍数是平年；
# 2. 公元年份为 4 的倍数但非 100 的倍数是闰年；
# 3. 公元年份为 400 的倍数是闰年。
# (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("\n--- 5.3 Leap Year Check ---")
year_to_check_str = "2024" # 假设输入
year_to_check = int(year_to_check_str)

# 确保年份大于1582 (在实际应用中应有此检查)
if year_to_check > 1582:
    is_leap = (year_to_check % 4 == 0 and year_to_check % 100 != 0) or \
              (year_to_check % 400 == 0)
    print(f'{year_to_check} is a leap year: {is_leap}') # Python 3.8+ f-string: print(f'{is_leap = }')
else:
    print(f"The Gregorian calendar rules apply for years after 1582. {year_to_check} is not applicable.")

year_2000 = 2000
is_leap_2000 = (year_2000 % 4 == 0 and year_2000 % 100 != 0) or (year_2000 % 400 == 0)
print(f"Is 2000 a leap year? {is_leap_2000}") # True (divisible by 400)

year_1900 = 1900
is_leap_1900 = (year_1900 % 4 == 0 and year_1900 % 100 != 0) or (year_1900 % 400 == 0)
print(f"Is 1900 a leap year? {is_leap_1900}") # False (divisible by 100 but not by 400)

year_2023 = 2023
is_leap_2023 = (year_2023 % 4 == 0 and year_2023 % 100 != 0) or (year_2023 % 400 == 0)
print(f"Is 2023 a leap year? {is_leap_2023}") # False (not divisible by 4)


# -----------------------------------------------------------------------------
# 六、其他运算符 (原文表格中提到，但未详细展开的)
# -----------------------------------------------------------------------------
# 6.1 身份运算符 (Identity Operators): is, is not
# 比较的是两个变量是否引用内存中的同一个对象。
print("\n--- 6.1 Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")  # False (内容相同，但内存地址不同)
print(f"list1 == list2: {list1 == list2}")  # True (内容相同)
print(f"list1 is list3: {list1 is list3}")  # True (list3是list1的引用)
print(f"list1 is not list2: {list1 is not list2}") # True

# 对于小的整数和一些字符串，Python为了优化可能会缓存它们，导致它们'is'为True
x_small_int = 5
y_small_int = 5
print(f"x_small_int ({x_small_int}) is y_small_int ({y_small_int}): {x_small_int is y_small_int}") # Usually True

# 6.2 成员运算符 (Membership Operators): in, not in
# 判断一个元素是否存在于一个序列（如字符串、列表、元组）中。
print("\n--- 6.2 Membership Operators ---")
my_string = "hello python"
my_list = [10, 20, 30, 40]

print(f"'h' in my_string: {'h' in my_string}")          # True
print(f"'world' in my_string: {'world' in my_string}")  # False
print(f"20 in my_list: {20 in my_list}")                # True
print(f"50 not in my_list: {50 not in my_list}")        # True

# 6.3 按位运算符 (Bitwise Operators): ~, &, |, ^, >>, << (原文表格提及)
# 对整数进行二进制位级别的操作。
# ~ (按位取反), & (按位与), | (按位或), ^ (按位异或)
# >> (右移), << (左移)
# 这些通常在底层编程或特定算法中使用。
print("\n--- 6.3 Bitwise Operators (Examples) ---")
num_a = 60  # 二进制: 0011 1100
num_b = 13  # 二进制: 0000 1101

print(f"~{num_a} (binary ~{bin(num_a)}): {~num_a} (binary {bin(~num_a)})") # -61 (按位取反)
# ~x = -(x+1)

print(f"{num_a} & {num_b} (binary {bin(num_a)} & {bin(num_b)}): {num_a & num_b} (binary {bin(num_a & num_b)})") # 12 (0000 1100)

print(f"{num_a} | {num_b} (binary {bin(num_a)} | {bin(num_b)}): {num_a | num_b} (binary {bin(num_a | num_b)})") # 61 (0011 1101)

print(f"{num_a} ^ {num_b} (binary {bin(num_a)} ^ {bin(num_b)}): {num_a ^ num_b} (binary {bin(num_a ^ num_b)})") # 49 (0011 0001)

print(f"{num_a} << 2 (binary {bin(num_a)} << 2): {num_a << 2} (binary {bin(num_a << 2)})") # 240 (1111 0000) (左移2位，相当于乘以2^2)

print(f"{num_a} >> 2 (binary {bin(num_a)} >> 2): {num_a >> 2} (binary {bin(num_a >> 2)})") # 15 (0000 1111) (右移2位，相当于整除2^2)

# -----------------------------------------------------------------------------
# 运算符优先级表格中提及但未在代码中显式演示的：
# `[]`, `[:]`: 索引和切片 (通常用于列表、字符串等序列类型，后续课程会详细讲解)
# -----------------------------------------------------------------------------

print("\n--- End of Day 04 Operators Demo ---")