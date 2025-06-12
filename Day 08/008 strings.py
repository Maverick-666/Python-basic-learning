# day_11_strings.py

# -----------------------------------------------------------------------------
# 核心概念：字符串 (String)
# - 由零个或多个字符组成的有限序列。
# - 不可变类型 (immutable)。
# - 定义：使用单引号 '', 双引号 "", 或三引号 ''' ''' / """ """。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、字符串的定义
# -----------------------------------------------------------------------------
print("--- 1. 字符串的定义 ---")
s1_d11_def = 'hello, world!'
s2_d11_def = "你好，世界！❤️"
s3_d11_def = '''hello,
wonderful
world!''' # 三引号字符串可以跨行
print(f"s1_d11_def: {s1_d11_def}")
print(f"s2_d11_def: {s2_d11_def}")
print(f"s3_d11_def:\n{s3_d11_def}")

# 1.1 转义字符 (\)
# \n: 换行, \t: 制表符, \': 单引号, \": 双引号, \\: 反斜杠本身
print("\n--- 1.1 转义字符 ---")
s_escape1_d11 = '\'hello, world!\'' # 'hello, world!'
s_escape2_d11 = '\\hello, world!\\' # \hello, world!\
s_escape3_d11 = "Line1\nLine2\tTabbed"
print(f"s_escape1_d11: {s_escape1_d11}")
print(f"s_escape2_d11: {s_escape2_d11}")
print(f"s_escape3_d11:\n{s_escape3_d11}")

# 1.2 原始字符串 (r'' 或 R'')
# 字符串中的每个字符都是它本来的含义，没有转义。
print("\n--- 1.2 原始字符串 ---")
s_raw1_d11 = '\it \is \time \to \read \now' # \t, \r, \n 会被转义
s_raw2_d11 = r'\it \is \time \to \read \now' # 所有字符按原样处理
print(f"s_raw1_d11 (normal):\n{s_raw1_d11}")
print(f"s_raw2_d11 (raw):\n{s_raw2_d11}")

# 1.3 字符的特殊表示
# \ooo: 八进制表示字符
# \xhh: 十六进制表示字符
# \uxxxx 或 \Uxxxxxxxx: Unicode编码表示字符
print("\n--- 1.3 字符的特殊表示 ---")
s_special1_d11 = '\141\142\143\x61\x62\x63' # 'abcabc' (a=oct 141 = hex 61)
s_special2_d11 = '\u9a86\u660a'             # '骆昊'
print(f"s_special1_d11: {s_special1_d11}")
print(f"s_special2_d11: {s_special2_d11}")
print("\n")

# -----------------------------------------------------------------------------
# 二、字符串的运算 (与列表/元组部分类似，但字符串不可变)
# -----------------------------------------------------------------------------
print("--- 2. 字符串的运算 ---")

# 2.1 拼接 (+) 和重复 (*)
print("--- 2.1 拼接和重复 ---")
str_concat1_d11 = 'hello' + ', ' + 'world'
print(f"Concatenated: {str_concat1_d11}") # hello, world
str_repeat_d11 = '!' * 3
print(f"Repeated: {str_repeat_d11}")       # !!!
str_concat1_d11 += str_repeat_d11          # 就地拼接 (实际是创建新字符串赋回)
print(f"After +=: {str_concat1_d11}")      # hello, world!!!
str_concat1_d11 *= 2                       # 就地重复
print(f"After *= 2: {str_concat1_d11}")    # hello, world!!!hello, world!!!

# 2.2 比较运算 (==, !=, <, <=, >, >=)
# 比较字符的编码大小 (字典序)
print("\n--- 2.2 比较运算 ---")
s_cmp1_d11 = 'apple'
s_cmp2_d11 = 'apply'
s_cmp3_d11 = 'Apple'
print(f"'{s_cmp1_d11}' == 'apple': {s_cmp1_d11 == 'apple'}") # True
print(f"'{s_cmp1_d11}' < '{s_cmp2_d11}': {s_cmp1_d11 < s_cmp2_d11}") # True ('e' < 'y')
print(f"'{s_cmp1_d11}' > '{s_cmp3_d11}': {s_cmp1_d11 > s_cmp3_d11}") # True ('a' > 'A')
print(f"ord('A')={ord('A')}, ord('a')={ord('a')}") # 65, 97
print(f"ord('骆')={ord('骆')}, ord('昊')={ord('昊')}")

# 2.3 成员运算 (in, not in)
print("\n--- 2.3 成员运算 ---")
s_member_d11 = 'hello, python world'
print(f"'python' in s_member_d11: {'python' in s_member_d11}")   # True
print(f"'java' not in s_member_d11: {'java' not in s_member_d11}") # True

# 2.4 获取字符串长度 (len())
print("\n--- 2.4 获取字符串长度 ---")
print(f"Length of '{s_member_d11}': {len(s_member_d11)}")

# 2.5 索引和切片 (与列表/元组类似，但返回的是字符串)
# 字符串是不可变的，不能通过索引或切片赋值修改原字符串。
print("\n--- 2.5 索引和切片 ---")
s_idx_slice_d11 = 'abc123456'
n_len_d11 = len(s_idx_slice_d11)
print(f"s_idx_slice_d11[0]: {s_idx_slice_d11[0]}")         # 'a'
print(f"s_idx_slice_d11[-1]: {s_idx_slice_d11[-1]}")       # '6'
print(f"s_idx_slice_d11[2:5]: {s_idx_slice_d11[2:5]}")     # 'c12'
print(f"s_idx_slice_d11[::2]: {s_idx_slice_d11[::2]}")     # 'ac246'
print(f"s_idx_slice_d11[::-1]: {s_idx_slice_d11[::-1]}")   # '654321cba'
# s_idx_slice_d11[0] = 'X' # TypeError: 'str' object does not support item assignment
print("\n")

# -----------------------------------------------------------------------------
# 三、字符的遍历
# -----------------------------------------------------------------------------
print("--- 3. 字符的遍历 ---")
s_iterate_d11 = 'hello'
print("方式一 (索引):")
for i_iter_d11 in range(len(s_iterate_d11)):
    print(s_iterate_d11[i_iter_d11], end=" ")
print("\n方式二 (直接元素):")
for char_iter_d11 in s_iterate_d11:
    print(char_iter_d11, end=" ")
print("\n\n")

# -----------------------------------------------------------------------------
# 四、字符串的方法 (String Methods)
# 由于字符串不可变，方法操作通常返回新的字符串，原字符串不变。
# -----------------------------------------------------------------------------
print("--- 4. 字符串的方法 ---")

# 4.1 大小写相关操作
print("--- 4.1 大小写相关 ---")
s_case_d11 = 'hELLo, wORLd!'
print(f"Original: '{s_case_d11}'")
print(f".capitalize(): '{s_case_d11.capitalize()}'") # 'Hello, world!'
print(f".title(): '{s_case_d11.title()}'")          # 'Hello, World!'
print(f".upper(): '{s_case_d11.upper()}'")          # 'HELLO, WORLD!'
print(f".lower(): '{s_case_d11.lower()}'")          # 'hello, world!'
print(f"Original s_case_d11 is still: '{s_case_d11}'") # 原字符串不变

# 4.2 查找操作
print("\n--- 4.2 查找操作 ---")
s_find_d11 = 'one two three two one'
print(f"s_find_d11.find('two'): {s_find_d11.find('two')}")         # 4 (首次出现)
print(f"s_find_d11.find('two', 5): {s_find_d11.find('two', 5)}")   # 14 (从索引5开始找)
print(f"s_find_d11.find('four'): {s_find_d11.find('four')}")       # -1 (未找到)
print(f"s_find_d11.index('two'): {s_find_d11.index('two')}")       # 4
# print(s_find_d11.index('four')) # ValueError: substring not found

print(f"s_find_d11.rfind('two'): {s_find_d11.rfind('two')}")       # 14 (从右边开始找首次出现)
print(f"s_find_d11.rindex('two'): {s_find_d11.rindex('two')}")     # 14

# 4.3 性质判断 (is... methods)
print("\n--- 4.3 性质判断 ---")
s_prop1_d11 = 'HelloWorld'
s_prop2_d11 = 'hello world' # 包含空格
s_prop3_d11 = '12345'
s_prop4_d11 = 'HelloWorld123'
print(f"'{s_prop1_d11}'.startswith('Hello'): {s_prop1_d11.startswith('Hello')}") # True
print(f"'{s_prop1_d11}'.endswith('World'): {s_prop1_d11.endswith('World')}")   # True
print(f"'{s_prop3_d11}'.isdigit(): {s_prop3_d11.isdigit()}")     # True (纯数字)
print(f"'{s_prop1_d11}'.isalpha(): {s_prop1_d11.isalpha()}")     # True (纯字母)
print(f"'{s_prop2_d11}'.isalpha(): {s_prop2_d11.isalpha()}")     # False (含空格)
print(f"'{s_prop4_d11}'.isalnum(): {s_prop4_d11.isalnum()}")     # True (字母或数字)
print(f"'{s_prop2_d11}'.isspace(): {'   '.isspace()}")          # True (纯空白字符)
print(f"'{s_prop1_d11}'.islower(): {s_prop1_d11.islower()}")     # False
print(f"'{s_prop1_d11.lower()}'.islower(): {s_prop1_d11.lower().islower()}") # True
print(f"'{s_prop1_d11}'.isupper(): {s_prop1_d11.isupper()}")     # False
print(f"'{s_prop1_d11.upper()}'.isupper(): {s_prop1_d11.upper().isupper()}") # True
print(f"'{s_case_d11.title()}'.istitle(): {s_case_d11.title().istitle()}")# True

# 4.4 格式化 (alignment and fill)
print("\n--- 4.4 格式化 (对齐与填充) ---")
s_format_align_d11 = 'text'
print(f"'{s_format_align_d11}'.center(10, '*'): '{s_format_align_d11.center(10, '*')}'") # ***text***
print(f"'{s_format_align_d11}'.ljust(10, '-'): '{s_format_align_d11.ljust(10, '-')}'")   # text------
print(f"'{s_format_align_d11}'.rjust(10, '+'): '{s_format_align_d11.rjust(10, '+')}'")   # ++++++text
print(f"'42'.zfill(5): '{'42'.zfill(5)}'")             # 00042
print(f"'-42'.zfill(5): '{'-42'.zfill(5)}'")           # -0042

# 4.4.1 格式化字符串 (%, .format(), f-string)
print("\n--- 4.4.1 格式化字符串 ---")
name_fmt_d11 = "Alice"
age_fmt_d11 = 30
# %-formatting (old style)
print("Name: %s, Age: %d" % (name_fmt_d11, age_fmt_d11))
# str.format() method
print("Name: {}, Age: {}".format(name_fmt_d11, age_fmt_d11))
print("Name: {n}, Age: {a}".format(n=name_fmt_d11, a=age_fmt_d11))
# f-string (formatted string literals, Python 3.6+) - recommended
print(f"Name: {name_fmt_d11}, Age: {age_fmt_d11}")

# f-string advanced formatting
pi_val_d11 = 3.1415926535
print(f"Pi (2 decimal places): {pi_val_d11:.2f}")      # 3.14
print(f"Number (10 wide, 0-padded): {42:0>10d}")     # 0000000042
print(f"Percentage: {0.25:.1%}")                      # 25.0%
print(f"Scientific notation: {1234567890:.2e}")       # 1.23e+09

# 4.5 修剪操作 (strip, lstrip, rstrip)
print("\n--- 4.5 修剪操作 ---")
s_strip1_d11 = '   whitespace   '
s_strip2_d11 = '---content---'
print(f"'{s_strip1_d11}'.strip(): '{s_strip1_d11.strip()}'")          # 'whitespace'
print(f"'{s_strip2_d11}'.strip('-'): '{s_strip2_d11.strip('-')}'")    # 'content'
print(f"'{s_strip1_d11}'.lstrip(): '{s_strip1_d11.lstrip()}'")        # 'whitespace   '
print(f"'{s_strip1_d11}'.rstrip(): '{s_strip1_d11.rstrip()}'")        # '   whitespace'

# 4.6 替换操作 (replace)
print("\n--- 4.6 替换操作 ---")
s_replace_d11 = 'one fish, two fish, red fish, blue fish'
print(f"Replace 'fish' with 'bird': '{s_replace_d11.replace('fish', 'bird')}'")
print(f"Replace 'fish' with 'bird' (max 2 times): '{s_replace_d11.replace('fish', 'bird', 2)}'")

# 4.7 拆分 (split) 与 合并 (join)
print("\n--- 4.7 拆分与合并 ---")
s_split_join_d11 = 'alpha,beta,gamma,delta'
parts_d11 = s_split_join_d11.split(',') # 拆分成列表
print(f"Split by ',': {parts_d11}")     # ['alpha', 'beta', 'gamma', 'delta']
merged_d11 = '-'.join(parts_d11)        # 用 '-' 合并列表中的字符串
print(f"Joined with '-': {merged_d11}") # alpha-beta-gamma-delta

s_split_limit_d11 = 'word1 word2 word3 word4'
print(f"Split with limit 2: {s_split_limit_d11.split(' ', 2)}") # ['word1', 'word2', 'word3 word4']

# 4.8 编码 (encode) 和 解码 (decode)
# str (Unicode) <-> bytes (binary data)
print("\n--- 4.8 编码和解码 ---")
str_unicode_d11 = '你好世界'
bytes_utf8_d11 = str_unicode_d11.encode('utf-8')
bytes_gbk_d11 = str_unicode_d11.encode('gbk')
print(f"'{str_unicode_d11}' encoded to UTF-8: {bytes_utf8_d11}") # b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c'
print(f"'{str_unicode_d11}' encoded to GBK: {bytes_gbk_d11}")   # b'\xc4\xe3\xba\xc3\xca\xc0\xbd\xe7'

decoded_from_utf8_d11 = bytes_utf8_d11.decode('utf-8')
decoded_from_gbk_d11 = bytes_gbk_d11.decode('gbk')
print(f"Decoded from UTF-8: {decoded_from_utf8_d11}")
print(f"Decoded from GBK: {decoded_from_gbk_d11}")
# bytes_utf8_d11.decode('gbk') # UnicodeDecodeError if encoding/decoding mismatch

# 4.9 其他方法 (如正则表达式 re 模块，后续课程)
print("\n")

print("--- End of Day 11 Strings Demo ---")