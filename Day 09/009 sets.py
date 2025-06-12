# day_12_sets.py

# -----------------------------------------------------------------------------
# 核心概念：集合 (Set)
# - 容器型数据类型，存储多个元素。
# - 特性：无序性 (unordered), 互异性 (distinct elements), 确定性。
# - 不支持索引运算。
# - 不能有重复元素。
# - 成员运算 (in, not in) 性能优于列表。
# - 底层使用哈希存储，元素必须是 hashable 类型 (不可变类型通常是)。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、创建集合
# -----------------------------------------------------------------------------
print("--- 1. 创建集合 ---")

# 1.1 使用 {} 字面量语法 (至少有一个元素)
set1_d12 = {1, 2, 3, 3, 3, 2} # 重复元素会被自动忽略
print(f"set1_d12 (from literals): {set1_d12}") # {1, 2, 3} (顺序可能不同)

set2_d12 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(f"set2_d12 (from literals): {set2_d12}") # {'grape', 'apple', 'pitaya', 'banana'} (顺序可能不同)

# {} 表示空字典，不是空集合。
empty_dict_d12 = {}
print(f"Type of {{}}: {type(empty_dict_d12)}") # <class 'dict'>

# 1.2 使用 set() 构造器
# - 创建空集合: set()
# - 将其他序列转换为集合
empty_set_d12 = set()
print(f"empty_set_d12: {empty_set_d12}, type: {type(empty_set_d12)}") # set()

set3_d12 = set('hello') # 字符串转集合
print(f"set3_d12 (from 'hello'): {set3_d12}") # {'o', 'e', 'h', 'l'} (顺序可能不同, 'l'只有一个)

set4_d12 = set([1, 2, 2, 3, 3, 3, 2, 1]) # 列表转集合
print(f"set4_d12 (from list): {set4_d12}") # {1, 2, 3}

# 1.3 使用集合生成式
set5_d12 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
# 1-19中，3的倍数或7的倍数
# 3, 6, 9, 12, 15, 18
# 7, 14
print(f"set5_d12 (from comprehension): {set5_d12}")
# {3, 6, 7, 9, 12, 14, 15, 18} (顺序可能不同)

# 1.4 集合元素必须是 hashable
# set_with_list_d12 = {1, 2, [3, 4]} # TypeError: unhashable type: 'list'
# set_with_set_d12 = {{1,2}, {3,4}} # TypeError: unhashable type: 'set'
set_with_tuple_d12 = {1, 2, (3, 4)} # 元组是 hashable 的
print(f"Set with tuple element: {set_with_tuple_d12}")
print("\n")

# -----------------------------------------------------------------------------
# 二、元素的遍历
# -----------------------------------------------------------------------------
print("--- 2. 元素的遍历 ---")
set_iterate_d12 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
print(f"Length of set_iterate_d12: {len(set_iterate_d12)}")

print("Iterating through set_iterate_d12:")
for elem_d12 in set_iterate_d12:
    print(elem_d12, end=" ") # 输出顺序不固定
print("\n\n")

# -----------------------------------------------------------------------------
# 三、集合的运算
# -----------------------------------------------------------------------------
print("--- 3. 集合的运算 ---")

# 3.1 成员运算 (in, not in)
set_member_ops1_d12 = {11, 12, 13, 14, 15}
print(f"10 in set_member_ops1_d12: {10 in set_member_ops1_d12}")      # False
print(f"15 in set_member_ops1_d12: {15 in set_member_ops1_d12}")      # True

set_member_ops2_d12 = {'Python', 'Java', 'C++', 'Swift'}
print(f"'Ruby' in set_member_ops2_d12: {'Ruby' in set_member_ops2_d12}")  # False
print(f"'Java' in set_member_ops2_d12: {'Java' in set_member_ops2_d12}")  # True

# 3.2 二元运算 (交集, 并集, 差集, 对称差)
print("\n--- 3.2 二元运算 ---")
set_op1_d12 = {1, 2, 3, 4, 5, 6, 7}
set_op2_d12 = {2, 4, 6, 8, 10}

# 交集 (& or intersection())
print(f"set_op1_d12 & set_op2_d12: {set_op1_d12 & set_op2_d12}") # {2, 4, 6}
print(f"set_op1_d12.intersection(set_op2_d12): {set_op1_d12.intersection(set_op2_d12)}")

# 并集 (| or union())
print(f"set_op1_d12 | set_op2_d12: {set_op1_d12 | set_op2_d12}") # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(f"set_op1_d12.union(set_op2_d12): {set_op1_d12.union(set_op2_d12)}")

# 差集 (- or difference())
print(f"set_op1_d12 - set_op2_d12 (op1 diff op2): {set_op1_d12 - set_op2_d12}") # {1, 3, 5, 7}
print(f"set_op1_d12.difference(set_op2_d12): {set_op1_d12.difference(set_op2_d12)}")
print(f"set_op2_d12 - set_op1_d12 (op2 diff op1): {set_op2_d12 - set_op1_d12}") # {8, 10}

# 对称差 (^ or symmetric_difference())
# (A | B) - (A & B) or (A - B) | (B - A)
print(f"set_op1_d12 ^ set_op2_d12: {set_op1_d12 ^ set_op2_d12}") # {1, 3, 5, 7, 8, 10}
print(f"set_op1_d12.symmetric_difference(set_op2_d12): {set_op1_d12.symmetric_difference(set_op2_d12)}")

# 3.3 复合赋值运算 (|=, &=, -=, ^=)
print("\n--- 3.3 复合赋值运算 ---")
set_compound1_d12 = {1, 3, 5, 7}
set_compound2_d12 = {2, 4, 6}
print(f"Original set_compound1_d12: {set_compound1_d12}")
set_compound1_d12 |= set_compound2_d12 # set_compound1_d12 = set_compound1_d12 | set_compound2_d12
# or set_compound1_d12.update(set_compound2_d12)
print(f"After |= set_compound2_d12: {set_compound1_d12}") # {1, 2, 3, 4, 5, 6, 7}

set_compound3_d12 = {3, 6, 9}
print(f"Original set_compound1_d12 (before &=): {set_compound1_d12}")
set_compound1_d12 &= set_compound3_d12 # set_compound1_d12 = set_compound1_d12 & set_compound3_d12
# or set_compound1_d12.intersection_update(set_compound3_d12)
print(f"After &= set_compound3_d12: {set_compound1_d12}") # {3, 6}

# set_compound1_d12 is now {3,6}
# set_compound2_d12 is {2,4,6}
print(f"Original set_compound2_d12: {set_compound2_d12}")
set_compound2_d12 -= set_compound1_d12 # set_compound2_d12 = set_compound2_d12 - set_compound1_d12
# or set_compound2_d12.difference_update(set_compound1_d12)
print(f"set_compound2_d12 After -= set_compound1_d12 (which is {{3,6}}): {set_compound2_d12}") # {2, 4} (6被减掉)

# 3.4 比较运算 (==, !=, <, <=, >, >=, issubset, issuperset)
print("\n--- 3.4 比较运算 ---")
set_cmp1_d12 = {1, 3, 5}
set_cmp2_d12 = {1, 2, 3, 4, 5}
set_cmp3_d12 = {5, 4, 3, 2, 1} # 顺序不同，但元素与 set_cmp2_d12 相同

print(f"set_cmp1_d12 < set_cmp2_d12 (is proper subset): {set_cmp1_d12 < set_cmp2_d12}")     # True
print(f"set_cmp1_d12 <= set_cmp2_d12 (is subset): {set_cmp1_d12 <= set_cmp2_d12}")    # True
print(f"set_cmp2_d12 < set_cmp3_d12 (is proper subset): {set_cmp2_d12 < set_cmp3_d12}")     # False (they are equal)
print(f"set_cmp2_d12 <= set_cmp3_d12 (is subset): {set_cmp2_d12 <= set_cmp3_d12}")    # True
print(f"set_cmp2_d12 == set_cmp3_d12 (is equal): {set_cmp2_d12 == set_cmp3_d12}")      # True
print(f"set_cmp2_d12 > set_cmp1_d12 (is proper superset): {set_cmp2_d12 > set_cmp1_d12}")   # True

print(f"set_cmp1_d12.issubset(set_cmp2_d12): {set_cmp1_d12.issubset(set_cmp2_d12)}")      # True
print(f"set_cmp2_d12.issuperset(set_cmp1_d12): {set_cmp2_d12.issuperset(set_cmp1_d12)}")  # True
print("\n")

# -----------------------------------------------------------------------------
# 四、集合的方法 (修改集合)
# -----------------------------------------------------------------------------
print("--- 4. 集合的方法 ---")
set_methods_d12 = {1, 10, 100}
print(f"Original set_methods_d12: {set_methods_d12}")

# 4.1 添加元素 (add)
set_methods_d12.add(1000)
set_methods_d12.add(10000) # add已存在的元素不会改变集合
set_methods_d12.add(10)
print(f"After add(1000), add(10000), add(10): {set_methods_d12}")

# 4.2 删除元素 (discard, remove, pop)
# discard(elem): 如果元素存在则删除，不存在不做任何事。
set_methods_d12.discard(10)
set_methods_d12.discard(2000) # 2000不存在，无事发生
print(f"After discard(10) and discard(2000): {set_methods_d12}")

# remove(elem): 如果元素存在则删除，不存在则引发 KeyError。
if 100 in set_methods_d12:
    set_methods_d12.remove(100)
# set_methods_d12.remove(3000) # KeyError: 3000
print(f"After remove(100): {set_methods_d12}")

# pop(): 随机删除并返回一个元素。如果集合为空，引发 KeyError。
if set_methods_d12: # 确保集合不为空
    popped_element_d12 = set_methods_d12.pop()
    print(f"Popped element: {popped_element_d12}")
    print(f"After pop(): {set_methods_d12}")

# 4.3 清空元素 (clear)
set_methods_d12.add(500) # 添加一个元素以便清空
print(f"Before clear: {set_methods_d12}")
set_methods_d12.clear()
print(f"After clear: {set_methods_d12}") # set()

# 4.4 判断两个集合是否没有交集 (isdisjoint)
print("\n--- 4.4 isdisjoint ---")
set_disjoint1_d12 = {'Java', 'Python', 'C++', 'Kotlin'}
set_disjoint2_d12 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set_disjoint3_d12 = {'HTML', 'CSS', 'JavaScript'}
print(f"set_disjoint1_d12.isdisjoint(set_disjoint2_d12): {set_disjoint1_d12.isdisjoint(set_disjoint2_d12)}") # False
print(f"set_disjoint1_d12.isdisjoint(set_disjoint3_d12): {set_disjoint1_d12.isdisjoint(set_disjoint3_d12)}") # True
print("\n")

# -----------------------------------------------------------------------------
# 五、不可变集合 (frozenset)
# - 不可变版本的集合，因此是 hashable 的，可以作为集合的元素或字典的键。
# - 除了不能添加和删除元素，其他运算与 set 类似。
# -----------------------------------------------------------------------------
print("--- 5. 不可变集合 (frozenset) ---")
fset1_d12 = frozenset({1, 3, 5, 7})
fset2_d12 = frozenset(range(1, 6)) # frozenset({1, 2, 3, 4, 5})
print(f"fset1_d12: {fset1_d12}")
print(f"fset2_d12: {fset2_d12}")

print(f"fset1_d12 & fset2_d12 (intersection): {fset1_d12 & fset2_d12}") # frozenset({1, 3, 5})
print(f"fset1_d12 | fset2_d12 (union): {fset1_d12 | fset2_d12}")       # frozenset({1, 2, 3, 4, 5, 7})
print(f"fset1_d12 - fset2_d12 (difference): {fset1_d12 - fset2_d12}")   # frozenset({7})
print(f"fset1_d12 < fset2_d12 (is proper subset): {fset1_d12 < fset2_d12}") # False

# fset1_d12.add(9) # AttributeError: 'frozenset' object has no attribute 'add'

# frozenset 可以作为 set 的元素
set_of_frozensets_d12 = {fset1_d12, fset2_d12, frozenset({1,3})}
print(f"Set of frozensets: {set_of_frozensets_d12}")
print("\n")

print("--- End of Day 12 Sets Demo ---")
