# day_05_branch_structures.py

# -----------------------------------------------------------------------------
# 核心概念：分支结构 (Branch Structure) / 选择结构 (Selection Structure)
# 允许程序根据条件执行不同的代码路径。
# 关键字：if, elif, else
# Python 使用缩进 (通常4个空格) 来定义代码块，表示代码的层次结构。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、使用 if, elif, else 构造分支结构
# -----------------------------------------------------------------------------

# 1.1 简单的 if 结构
print("--- 1.1 Simple if structure ---")
# BMI 计算器: BMI = 体重(kg) / (身高(m))^2
# 正常范围: 18.5 <= BMI < 24
height_cm_v1 = 175.0 # 假设输入
weight_kg_v1 = 68.0  # 假设输入
bmi_v1 = weight_kg_v1 / (height_cm_v1 / 100) ** 2
print(f'{bmi_v1 = :.1f}') # Python 3.8+ f-string
if 18.5 <= bmi_v1 < 24: # Python 支持链式比较
    print('你的身材很棒！')

height_cm_v1_b = 175.0
weight_kg_v1_b = 95.0
bmi_v1_b = weight_kg_v1_b / (height_cm_v1_b / 100) ** 2
print(f'\n{bmi_v1_b = :.1f}')
if 18.5 <= bmi_v1_b < 24:
    print('你的身材很棒！') # 这句不会执行

# 1.2 if-else 结构
print("\n--- 1.2 if-else structure ---")
height_cm_v2 = 175.0
weight_kg_v2 = 95.0 # 体重过重
bmi_v2 = weight_kg_v2 / (height_cm_v2 / 100) ** 2
print(f'{bmi_v2 = :.1f}')
if 18.5 <= bmi_v2 < 24:
    print('你的身材很棒！')
else:
    print('你的身材不够标准哟！')

# 1.3 if-elif-else 结构 (多分支)
print("\n--- 1.3 if-elif-else structure ---")
height_cm_v3 = 175.0
weight_kg_v3 = 95.0 # 中度肥胖
bmi_v3 = weight_kg_v3 / (height_cm_v3 / 100) ** 2
print(f'{bmi_v3 = :.1f}')
if bmi_v3 < 18.5:
    print('你的体重过轻！')
elif bmi_v3 < 24: # 隐含条件: bmi_v3 >= 18.5
    print('你的身材很棒！')
elif bmi_v3 < 27: # 隐含条件: bmi_v3 >= 24
    print('你的体重过重！')
elif bmi_v3 < 30: # 隐含条件: bmi_v3 >= 27
    print('你已轻度肥胖！')
elif bmi_v3 < 35: # 隐含条件: bmi_v3 >= 30
    print('你已中度肥胖！')
else: # 隐含条件: bmi_v3 >= 35
    print('你已重度肥胖！')

# -----------------------------------------------------------------------------
# 二、使用 match 和 case 构造分支结构 (Python 3.10+)
# -----------------------------------------------------------------------------
# 适用于多分支，且每个分支基于特定值的匹配。

print("\n--- 2.1 match-case for HTTP status (original) ---")
status_code_v1 = 403 # 假设输入
# 使用 if-elif-else 实现
if status_code_v1 == 400:
    description_v1 = 'Bad Request'
elif status_code_v1 == 401:
    description_v1 = 'Unauthorized'
elif status_code_v1 == 403:
    description_v1 = 'Forbidden'
elif status_code_v1 == 404:
    description_v1 = 'Not Found'
elif status_code_v1 == 405:
    description_v1 = 'Method Not Allowed'
elif status_code_v1 == 418:
    description_v1 = 'I am a teapot'
elif status_code_v1 == 429:
    description_v1 = 'Too many requests'
else:
    description_v1 = 'Unknown status Code'
print(f'Status {status_code_v1} (using if-elif): {description_v1}')

print("\n--- 2.2 match-case for HTTP status ---")
status_code_v2 = 403 # 假设输入
# 使用 match-case 实现
match status_code_v2:
    case 400: description_v2 = 'Bad Request'
    case 401: description_v2 = 'Unauthorized'
    case 403: description_v2 = 'Forbidden'
    case 404: description_v2 = 'Not Found'
    case 405: description_v2 = 'Method Not Allowed'
    case 418: description_v2 = 'I am a teapot'
    case 429: description_v2 = 'Too many requests'
    case _: description_v2 = 'Unknown Status Code' # _ 是通配符，匹配任何其他情况
print(f'Status {status_code_v2} (using match-case): {description_v2}')

# 2.3 match-case 合并模式 (OR pattern)
print("\n--- 2.3 match-case with OR pattern ---")
status_code_v3 = 403 # 假设输入
match status_code_v3:
    case 400 | 405: description_v3 = 'Invalid Request' # 匹配 400 或 405
    case 401 | 403 | 404: description_v3 = 'Not Allowed' # 匹配 401 或 403 或 404
    case 418: description_v3 = 'I am a teapot'
    case 429: description_v3 = 'Too many requests'
    case _: description_v3 = 'Unknown Status Code'
print(f'Status {status_code_v3} (match-case OR): {description_v3}')

status_code_v4 = 400
match status_code_v4:
    case 400 | 405: description_v4 = 'Invalid Request'
    case 401 | 403 | 404: description_v4 = 'Not Allowed'
    # ... (其他 case)
    case _: description_v4 = 'Unknown'
print(f'Status {status_code_v4} (match-case OR): {description_v4}')


# -----------------------------------------------------------------------------
# 三、分支结构的应用
# -----------------------------------------------------------------------------

# 3.1 分段函数求值
# y = 3x - 5,   (x > 1)
# y = x + 2,    (-1 <= x <= 1)
# y = 5x + 3,   (x < -1)
print("\n--- 3.1 Piecewise function evaluation (flat) ---")
x_val_v1 = 0.5 # 假设输入
if x_val_v1 > 1:
    y_val_v1 = 3 * x_val_v1 - 5
elif x_val_v1 >= -1: # 隐含 x_val_v1 <= 1
    y_val_v1 = x_val_v1 + 2
else: # 隐含 x_val_v1 < -1
    y_val_v1 = 5 * x_val_v1 + 3
print(f'For x = {x_val_v1}, y = {y_val_v1}')

print("\n--- 3.1.2 Piecewise function evaluation (nested) ---")
# 嵌套分支实现 (通常不推荐，扁平化更好 "Flat is better than nested")
x_val_v2 = 0.5 # 假设输入
if x_val_v2 > 1:
    y_val_v2 = 3 * x_val_v2 - 5
else: # x_val_v2 <= 1
    if x_val_v2 >= -1: # -1 <= x_val_v2 <= 1
        y_val_v2 = x_val_v2 + 2
    else: # x_val_v2 < -1
        y_val_v2 = 5 * x_val_v2 + 3
print(f'For x = {x_val_v2} (nested), y = {y_val_v2}')


# 3.2 百分制成绩转换成等级
# >= 90: A
# >= 80: B
# >= 70: C
# >= 60: D
# < 60: E
print("\n--- 3.2 Grade conversion ---")
score_v1 = 85.0 # 假设输入
if score_v1 >= 90:
    grade_v1 = 'A'
elif score_v1 >= 80: # 隐含 score_v1 < 90
    grade_v1 = 'B'
elif score_v1 >= 70: # 隐含 score_v1 < 80
    grade_v1 = 'C'
elif score_v1 >= 60: # 隐含 score_v1 < 70
    grade_v1 = 'D'
else: # 隐含 score_v1 < 60
    grade_v1 = 'E'
print(f'Score {score_v1} corresponds to grade: {grade_v1}')


# 3.3 计算三角形的周长和面积
# 条件: 任意两边之和大于第三边 (a+b>c, a+c>b, b+c>a)
# 面积: 海伦公式 A = sqrt(s(s-a)(s-b)(s-c)), s = (a+b+c)/2
print("\n--- 3.3 Triangle calculations ---")
side_a = 3.0 # 假设输入
side_b = 4.0 # 假设输入
side_c = 5.0 # 假设输入 (构成直角三角形)

if side_a + side_b > side_c and \
   side_a + side_c > side_b and \
   side_b + side_c > side_a:
    perimeter = side_a + side_b + side_c
    print(f'Perimeter: {perimeter}')
    s_half_perimeter = perimeter / 2
    # area = (s_half_perimeter * (s_half_perimeter - side_a) * \
    #         (s_half_perimeter - side_b) * (s_half_perimeter - side_c)) ** 0.5
    # 更健壮的写法，避免负数开方（虽然在此例中不会发生，但浮点数精度可能导致问题）
    term_a = s_half_perimeter - side_a
    term_b = s_half_perimeter - side_b
    term_c = s_half_perimeter - side_c
    if term_a < 0 or term_b < 0 or term_c < 0: # 理论上如果构成三角形，这不会发生
        print("Error in Heron's formula terms (should not happen for valid triangle).")
        area = float('nan') # Not a Number
    else:
        area = (s_half_perimeter * term_a * term_b * term_c) ** 0.5
    print(f'Area: {area:.2f}')
else:
    print('The given sides cannot form a triangle.')

side_a2, side_b2, side_c2 = 1.0, 2.0, 5.0 # 不能构成三角形
if side_a2 + side_b2 > side_c2 and \
   side_a2 + side_c2 > side_b2 and \
   side_b2 + side_c2 > side_a2:
    print("\nThis part should not be reached for 1,2,5")
else:
    print(f'\nSides {side_a2}, {side_b2}, {side_c2} cannot form a triangle.')

# -----------------------------------------------------------------------------
# 缩进和代码块
# 连续的、具有相同缩进级别的语句构成一个代码块。
# -----------------------------------------------------------------------------
print("\n--- Indentation Example ---")
test_value = 10
if test_value > 5:
    print("Value is greater than 5.") # 属于if块
    print("This is also part of the if block.") # 属于if块
    if test_value > 8:
        print("Value is also greater than 8.") # 属于嵌套的if块
        print("This is part of the nested if block.") # 属于嵌套的if块
    print("Back to the first if block.") # 属于第一个if块
print("This is outside any if block.") # 不属于任何if块

print("\n--- End of Day 05 Branch Structures Demo ---")