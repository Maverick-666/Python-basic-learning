# day_08_09_lists_combined.py

import random
# from rich.console import Console # For rich example, can be commented out if not installed
# from rich.table import Table     # For rich example

# -----------------------------------------------------------------------------

# 引入问题：统计掷色子点数出现的次数 (原始丑陋版)
# -----------------------------------------------------------------------------
print("--- 掷色子原始版 ---")
f1, f2, f3, f4, f5, f6 = 0, 0, 0, 0, 0, 0
# for _ in range(6000): # 模拟运行，减少次数
for _ in range(600):
    face_orig = random.randrange(1, 7)
    if face_orig == 1: f1 += 1
    elif face_orig == 2: f2 += 1
    elif face_orig == 3: f3 += 1
    elif face_orig == 4: f4 += 1
    elif face_orig == 5: f5 += 1
    else: f6 += 1
# print(f'1点出现了{f1}次')
# print(f'2点出现了{f2}次')
# ... (其他点数)
print(f'原始版模拟600次统计: 1点:{f1}, 2点:{f2}, 3点:{f3}, 4点:{f4}, 5点:{f5}, 6点:{f6}')
print("\n")

# -----------------------------------------------------------------------------

# 一、创建列表 (Creating Lists)
# 列表是由一系元素按特定顺序构成的数据序列，可以保存多个数据。
# -----------------------------------------------------------------------------
print("--- 1. 创建列表 ---")
# 1.1 使用 [] 字面量语法
items1_d8 = [35, 12, 99, 68, 55, 35, 87] # 可以有重复元素
items2_d8 = ['Python', 'Java', 'Go', 'Kotlin']
items3_d8 = [100, 12.3, 'Python', True]     # 可以有不同类型的元素 (但不推荐)
print(f"items1_d8: {items1_d8}")
print(f"items2_d8: {items2_d8}")
print(f"items3_d8: {items3_d8}")
print(f"Type of items1_d8: {type(items1_d8)}")

# 1.2 使用 list() 构造器将其他序列转为列表
items4_d8 = list(range(1, 10)) # range 对象转列表
items5_d8 = list('hello')      # 字符串转列表 (每个字符一个元素)
print(f"items4_d8 (from range): {items4_d8}")
print(f"items5_d8 (from string): {items5_d8}")
print("\n")

# -----------------------------------------------------------------------------

# 二、列表的运算 (List Operations)
# -----------------------------------------------------------------------------
print("--- 2. 列表的运算 ---")
list_a_d8 = [10, 20, 30]
list_b_d8 = [40, 50]
list_c_d8 = ['x', 'y']

# 2.1 拼接 (+)
print(f"list_a_d8 + list_b_d8: {list_a_d8 + list_b_d8}")
# list_a_d8 += list_c_d8 # 就地修改 list_a_d8
# print(f"list_a_d8 after += list_c_d8: {list_a_d8}") # [10, 20, 30, 'x', 'y']
# 为了后续演示，重新初始化 list_a_d8
list_a_d8 = [10, 20, 30]

# 2.2 重复 (*)
print(f"list_b_d8 * 3: {list_b_d8 * 3}")

# 2.3 成员运算 (in, not in)
print(f"20 in list_a_d8: {20 in list_a_d8}")       # True
print(f"'z' not in list_c_d8: {'z' not in list_c_d8}") # True

# 2.4 索引运算 ([index])
# 正向索引: 0 to N-1
# 反向索引: -1 to -N
items_idx_d8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(f"items_idx_d8[0]: {items_idx_d8[0]}")   # apple
print(f"items_idx_d8[-1]: {items_idx_d8[-1]}") # watermelon
items_idx_d8[2] = 'durian' # 修改元素
print(f"items_idx_d8 after modification: {items_idx_d8}")
# print(items_idx_d8[5]) # IndexError: list index out of range

# 2.5 切片运算 ([start:end:stride])
# start: 起始位置 (包含)
# end: 终止位置 (不包含)
# stride: 步长 (默认为1)
items_slice_d8 = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"items_slice_d8[1:4]: {items_slice_d8[1:4]}")         # ['b', 'c', 'd']
print(f"items_slice_d8[:3]: {items_slice_d8[:3]}")          # ['a', 'b', 'c'] (start省略，默认为0)
print(f"items_slice_d8[3:]: {items_slice_d8[3:]}")          # ['d', 'e', 'f'] (end省略，默认为列表长度)
print(f"items_slice_d8[::2]: {items_slice_d8[::2]}")        # ['a', 'c', 'e'] (stride为2)
print(f"items_slice_d8[::-1]: {items_slice_d8[::-1]}")      # ['f', 'e', 'd', 'c', 'b', 'a'] (反转列表)
print(f"items_slice_d8[-3:-1]: {items_slice_d8[-3:-1]}")    # ['d', 'e']
items_slice_d8[1:3] = ['X', 'Y'] # 切片赋值
print(f"items_slice_d8 after slice assignment: {items_slice_d8}") # ['a', 'X', 'Y', 'd', 'e', 'f']

# 2.6 关系运算 (==, !=, <, <=, >, >=)
# 按字典序逐个比较元素
nums1_d8 = [1, 2, 3]
nums2_d8 = list(range(1, 4))
nums3_d8 = [1, 2, 4]
print(f"nums1_d8 == nums2_d8: {nums1_d8 == nums2_d8}") # True
print(f"nums1_d8 < nums3_d8: {nums1_d8 < nums3_d8}")   # True (因为 3 < 4)
print("\n")

# -----------------------------------------------------------------------------

# 三、元素的遍历 (Iterating Through Elements)
# -----------------------------------------------------------------------------
print("---  3. 元素的遍历 ---")
languages_d8 = ['Python', 'Java', 'C++', 'Kotlin']

# 3.1 方法一：通过索引遍历
print("遍历方法一 (索引):")
for index_d8 in range(len(languages_d8)):
    print(languages_d8[index_d8])

# 3.2 方法二：直接遍历元素 (推荐)
print("\n遍历方法二 (直接元素):")
for language_d8 in languages_d8:
    print(language_d8)
print("\n")

# -----------------------------------------------------------------------------
#
# 四、使用列表重构掷色子统计代码
# -----------------------------------------------------------------------------
print("---  4. 重构掷色子统计 ---")
counters_d8 = [0] * 6 # 创建包含6个0的列表 [0, 0, 0, 0, 0, 0]
# for _ in range(6000): # 模拟运行，减少次数
for _ in range(600):
    face_d8 = random.randrange(1, 7) # 1 到 6
    counters_d8[face_d8 - 1] += 1 # 点数1对应索引0, 点数6对应索引5

for face_val_d8 in range(1, 7):
    print(f'{face_val_d8}点出现了{counters_d8[face_val_d8 - 1]}次')
print("\n")


# -----------------------------------------------------------------------------
#
# 五、列表的方法 (List Methods)
# -----------------------------------------------------------------------------
print("--- 5. 列表的方法 ---")

# 5.1 添加元素
print("--- 5.1 添加元素 ---")
langs_d9 = ['Python', 'Java', 'C++']
langs_d9.append('JavaScript') # 追加到末尾
print(f"After append: {langs_d9}")
langs_d9.insert(1, 'SQL')     # 在索引1处插入
print(f"After insert: {langs_d9}")

# 5.2 删除元素
print("\n--- 5.2 删除元素 ---")
# langs_d9 is now ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in langs_d9:
    langs_d9.remove('Java') # 删除第一个匹配的'Java'
print(f"After remove 'Java': {langs_d9}")

# pop([index]): 删除并返回指定索引的元素 (默认最后一个)
last_lang = langs_d9.pop()
print(f"Popped last element: {last_lang}")
print(f"List after pop(): {langs_d9}")
sql_lang = langs_d9.pop(1) # 删除索引1的元素
print(f"Popped element at index 1: {sql_lang}")
print(f"List after pop(1): {langs_d9}")

# clear(): 清空列表
# langs_d9.clear()
# print(f"After clear: {langs_d9}")
# 为了后续演示，重新赋值
langs_d9 = ['Python', 'C++']

# del 关键字删除元素
del langs_d9[0] # 删除索引0的元素
print(f"After del langs_d9[0]: {langs_d9}") # ['C++']

# 5.3 元素位置和频次
print("\n--- 5.3 元素位置和频次 ---")
items_count_idx_d9 = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(f"Index of 'Python': {items_count_idx_d9.index('Python')}")         # 0
print(f"Index of 'Python' (from index 1): {items_count_idx_d9.index('Python', 1)}") # 5
# print(items_count_idx_d9.index('Go')) # ValueError

print(f"Count of 'Java': {items_count_idx_d9.count('Java')}")     # 2
print(f"Count of 'Swift': {items_count_idx_d9.count('Swift')}")   # 0

# 5.4 元素排序和反转
print("\n--- 5.4 元素排序和反转 ---")
items_sort_rev_d9 = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items_sort_rev_d9.sort() # 就地排序 (默认升序)
print(f"After sort(): {items_sort_rev_d9}")
items_sort_rev_d9.sort(reverse=True) # 就地降序排序
print(f"After sort(reverse=True): {items_sort_rev_d9}")

items_sort_rev_d9.reverse() # 就地反转
print(f"After reverse(): {items_sort_rev_d9}")
print("\n")

# -----------------------------------------------------------------------------

# 六、列表生成式 (List Comprehensions)
# -----------------------------------------------------------------------------
print("---  6. 列表生成式 ---")

# 6.1 场景一：1-99中能被3或5整除的数
print("--- 6.1 Divisible by 3 or 5 ---")
# 传统方法
items_trad_s1 = []
for i_s1 in range(1, 100):
    if i_s1 % 3 == 0 or i_s1 % 5 == 0:
        items_trad_s1.append(i_s1)
# print(f"Traditional: {items_trad_s1}")
# 列表生成式
items_comp_s1 = [i_s1 for i_s1 in range(1, 100) if i_s1 % 3 == 0 or i_s1 % 5 == 0]
print(f"Comprehension: {items_comp_s1}")

# 6.2 场景二：列表中元素的平方
print("\n--- 6.2 Square of elements ---")
nums1_s2 = [35, 12, 97, 64, 55]
# 传统方法
# nums2_trad_s2 = []
# for num_s2 in nums1_s2:
#     nums2_trad_s2.append(num_s2 ** 2)
# 列表生成式
nums2_comp_s2 = [num_s2 ** 2 for num_s2 in nums1_s2]
print(f"Original: {nums1_s2}, Squared: {nums2_comp_s2}")

# 6.3 场景三：筛选大于50的元素
print("\n--- 6.3 Filter elements greater than 50 ---")
nums1_s3 = [35, 12, 97, 64, 55]
# 传统方法
# nums2_trad_s3 = []
# for num_s3 in nums1_s3:
#     if num_s3 > 50:
#         nums2_trad_s3.append(num_s3)
# 列表生成式
nums2_comp_s3 = [num_s3 for num_s3 in nums1_s3 if num_s3 > 50]
print(f"Original: {nums1_s3}, Filtered (>50): {nums2_comp_s3}")
print("\n")

# -----------------------------------------------------------------------------
# 七、嵌套列表 (Nested Lists)
# 列表中的元素也可以是列表，用于表示表格、矩阵等。
# -----------------------------------------------------------------------------
print("--- 7. 嵌套列表 ---")
scores_nested_d9 = [[95, 83, 92], [80, 75, 82], [92, 97, 90]]
print(f"Nested list (scores_nested_d9): {scores_nested_d9}")
print(f"First student's scores: {scores_nested_d9[0]}")       # [95, 83, 92]
print(f"First student's second score: {scores_nested_d9[0][1]}") # 83

# 7.1 通过键盘输入创建嵌套列表 (示例代码，实际运行时会暂停)
# scores_input_d9 = []
# print("\n--- Input for nested list (5 students, 3 scores each) ---")
# for _ in range(2): # 原文5，改为2便于测试
#     temp_scores_d9 = []
#     print(f"Enter scores for student {len(scores_input_d9) + 1}:")
#     for _ in range(3):
#         # score_val_d9 = int(input(f'  Enter score {len(temp_scores_d9) + 1}: '))
#         score_val_d9 = random.randint(60,100) # 模拟输入
#         temp_scores_d9.append(score_val_d9)
#     scores_input_d9.append(temp_scores_d9)
# print(f"Entered scores: {scores_input_d9}")

# 7.2 使用列表生成式创建嵌套列表 (随机成绩)
print("\n--- Nested list comprehension (random scores) ---")
# 5个学生，每人3门课成绩 (60-100)
scores_comp_nested_d9 = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(f"Generated scores (nested comprehension): {scores_comp_nested_d9}")
print("\n")

# -----------------------------------------------------------------------------

# 八、列表的应用：双色球随机选号
# 规则: 6个红球 (1-33, 不重复), 1个蓝球 (1-16)
# -----------------------------------------------------------------------------
print("---  8. 双色球随机选号 ---")

# 8.1 方法一：pop 从列表中移除 (模拟无放回抽样)
print("--- 8.1 Version 1.0 (using pop) ---")
red_balls_v1 = list(range(1, 34)) # 1 to 33
selected_red_v1 = []
for _ in range(6):
    index_v1 = random.randrange(len(red_balls_v1))
    selected_red_v1.append(red_balls_v1.pop(index_v1))
selected_red_v1.sort()
blue_ball_v1 = random.randrange(1, 17) # 1 to 16

# print("Selected red balls (v1):", end=" ")
# for ball in selected_red_v1: print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# print(f"Selected blue ball (v1): \033[034m{blue_ball_v1:0>2d}\033[0m\n")
# 简化输出，不带颜色
print(f"Selected red balls (v1): {selected_red_v1}")
print(f"Selected blue ball (v1): {blue_ball_v1}\n")


# 8.2 方法二：random.sample 和 random.choice (推荐)
print("--- 8.2 Version 1.1 (using sample and choice) ---")
red_balls_pool_v2 = list(range(1, 34))
blue_balls_pool_v2 = list(range(1, 17))

selected_red_v2 = random.sample(red_balls_pool_v2, 6) # 无放回抽样6个
selected_red_v2.sort()
blue_ball_v2 = random.choice(blue_balls_pool_v2)    # 随机选1个

print(f"Selected red balls (v2): {selected_red_v2}")
print(f"Selected blue ball (v2): {blue_ball_v2}\n")

# 8.3 方法三：生成N注号码
print("--- 8.3 Version 1.2 (generating N sets) ---")
num_sets = 3 # 原文用input，这里固定为3
# red_balls_pool_v3 = [i for i in range(1, 34)] # 列表生成式创建
# blue_balls_pool_v3 = [i for i in range(1, 17)]
print(f"Generating {num_sets} sets of lottery numbers:")
for i_set in range(num_sets):
    selected_red_v3 = random.sample(red_balls_pool_v2, 6) # 复用v2的球池
    selected_red_v3.sort()
    blue_ball_v3 = random.choice(blue_balls_pool_v2)
    print(f"Set {i_set + 1}: Red {selected_red_v3}, Blue [{blue_ball_v3}]")
print("\n")

# 8.4 方法四：使用 rich 库美化输出 (如果安装了rich库可以取消注释)
# print("--- 8.4 Version 1.3 (using rich library for pretty print) ---")
# console_rich = Console()
# num_sets_rich = 2 # int(input('生成几注号码 (rich): '))
# red_balls_rich = [i for i in range(1, 34)]
# blue_balls_rich = [i for i in range(1, 17)]
# table_rich = Table(show_header=True, header_style="bold magenta")
# table_rich.add_column("序号", justify="center")
# table_rich.add_column("红球", justify="center", style="red")
# table_rich.add_column("蓝球", justify="center", style="blue")

# for i_rich in range(num_sets_rich):
#     selected_red_rich = random.sample(red_balls_rich, 6)
#     selected_red_rich.sort()
#     blue_ball_rich = random.choice(blue_balls_rich)
#     table_rich.add_row(
#         str(i_rich + 1),
#         " ".join([f"{ball:0>2d}" for ball in selected_red_rich]),
#         f"{blue_ball_rich:0>2d}"
#     )
# console_rich.print(table_rich)


print("--- End of Day 08-09 Lists Combined Demo ---")