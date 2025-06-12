# day_03_variables.py

# -----------------------------------------------------------------------------
# 核心概念：程序是数据和指令的有序集合。
# Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、变量 (Variables)
# -----------------------------------------------------------------------------
# 变量是数据的载体，是用来保存数据的内存空间。
# 变量的值可以被读取和修改。

# 1.1 变量的赋值与读取
# 定义一个名为 'message' 的变量，并赋值为字符串 "Hello, Python learners!"
message = "Hello, Python learners!"
print(message)  # 读取并打印变量 message 的值

# 1.2 变量值的修改
student_count = 20
print("Initial student count:", student_count)
student_count = 25  # 修改变量 student_count 的值
print("Updated student count:", student_count)

# -----------------------------------------------------------------------------
# 二、数据类型 (Data Types)
# -----------------------------------------------------------------------------
# Python 中常见的数据类型

# 2.1 整型 (int)
# Python可以处理任意大小的整数。
# 支持多种进制表示法：

# 十进制整数 (Decimal)
decimal_number = 100
print("Decimal:", decimal_number, type(decimal_number))

# 二进制整数 (Binary) - 以 0b 或 0B 开头
binary_number = 0b1100100  # 对应十进制的 100
print("Binary (0b1100100):", binary_number, type(binary_number))

# 八进制整数 (Octal) - 以 0o 或 0O 开头
octal_number = 0o144  # 对应十进制的 100
print("Octal (0o144):", octal_number, type(octal_number))

# 十六进制整数 (Hexadecimal) - 以 0x 或 0X 开头
hexadecimal_number = 0x64  # 对应十进制的 100
print("Hexadecimal (0x64):", hexadecimal_number, type(hexadecimal_number))

# 2.2 浮点型 (float)
# 浮点数即小数。

# 数学写法
pi_approx = 3.14159
print("Float (math notation):", pi_approx, type(pi_approx))

# 科学计数法
speed_of_light = 2.99792458e8  # 2.99792458 * 10^8
print("Float (scientific notation):", speed_of_light, type(speed_of_light))

# 2.3 字符串型 (str)
# 字符串是以单引号或双引号包裹起来的任意文本。

string_single_quotes = 'Hello, world!'
string_double_quotes = "Python is fun."
print("String (single quotes):", string_single_quotes, type(string_single_quotes))
print("String (double quotes):", string_double_quotes, type(string_double_quotes))

# 字符串拼接示例 (原文未详述，作为补充案例)
greeting = "Good morning"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print("Concatenated string:", full_greeting)

# 2.4 布尔型 (bool)
# 布尔型只有 True 和 False 两种值。

is_learning = True
is_tired = False
print("Boolean (True):", is_learning, type(is_learning))
print("Boolean (False):", is_tired, type(is_tired))

# 布尔型在条件判断中的应用 (原文未详述，作为补充案例)
if is_learning:
    print("Keep up the good work!")
else:
    print("Time to learn something new!")

# -----------------------------------------------------------------------------
# 三、变量命名 (Variable Naming)
# -----------------------------------------------------------------------------
# 规则：
# 1. 变量名由字母（Unicode）、数字、下划线构成，数字不能开头。
#    建议：尽可能只使用英文字母、数字、下划线。
# 2. 大小写敏感 (e.g., 'age' 和 'Age' 是不同变量)。
# 3. 不要跟Python关键字重名 (e.g., 'if', 'for', 'while', 'True', 'False')。
#    避开Python保留字 (e.g., 'int', 'str', 'print')。

# 惯例：
# 1. 变量名通常使用小写英文字母，多个单词用下划线连接 (snake_case)。
#    (受保护的变量_开头，私有变量__开头，后续课程会讲)
# 2. 见名知意。

# 合法且推荐的变量名示例
user_name = "洞察先锋"
age = 30
has_completed_task = True
_internal_counter = 0 # 惯例：单个下划线开头表示受保护

# 不推荐或错误的变量名示例 (会引起错误或混淆，这里注释掉以防执行出错)
# 1_variable = 10      # 错误：数字开头
# user-name = "test"   # 错误：包含非法字符 '-'
# class = "Python"     # 错误：与关键字 'class' 重名
# True = False         # 错误：与关键字 'True' 重名

# 大小写敏感示例
my_variable = 10
My_Variable = 20
print("my_variable:", my_variable)
print("My_Variable:", My_Variable) # 这是另一个不同的变量

# -----------------------------------------------------------------------------
# 四、变量的使用 (Using Variables)
# -----------------------------------------------------------------------------

# 4.1 赋值与基本运算
num1 = 45
num2 = 12

print("num1:", num1)
print("num2:", num2)

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2 # 除法总是返回浮点数

print(f"{num1} + {num2} =", sum_result)
print(f"{num1} - {num2} =", difference_result)
print(f"{num1} * {num2} =", product_result)
print(f"{num1} / {num2} =", quotient_result)

# 4.2 使用 type() 函数检查变量类型
print("Type of num1:", type(num1))                # <class 'int'>
print("Type of quotient_result:", type(quotient_result)) # <class 'float'>
print("Type of user_name:", type(user_name))      # <class 'str'>
print("Type of is_learning:", type(is_learning))  # <class 'bool'>

# -----------------------------------------------------------------------------
# 五、类型转换 (Type Conversion)
# -----------------------------------------------------------------------------
# Python 内置函数进行类型转换

# 5.1 int() - 转换为整数
val_float_to_int = 123.789
converted_int_from_float = int(val_float_to_int) # 结果为 123 (截断小数部分)
print(f"float {val_float_to_int} to int: {converted_int_from_float}", type(converted_int_from_float))

val_str_to_int = "250"
converted_int_from_str = int(val_str_to_int)
print(f"string '{val_str_to_int}' to int: {converted_int_from_str}", type(converted_int_from_str))

# 字符串转整数时指定进制
str_hex = "1A" # 十六进制的 1A 是十进制的 26
int_from_hex_str = int(str_hex, base=16)
print(f"string '{str_hex}' (base 16) to int: {int_from_hex_str}", type(int_from_hex_str))

str_bin = "1101" # 二进制的 1101 是十进制的 13
int_from_bin_str = int(str_bin, base=2)
print(f"string '{str_bin}' (base 2) to int: {int_from_bin_str}", type(int_from_bin_str))

# 5.2 float() - 转换为浮点数
val_int_to_float = 77
converted_float_from_int = float(val_int_to_float) # 结果为 77.0
print(f"int {val_int_to_float} to float: {converted_float_from_int}", type(converted_float_from_int))

val_str_to_float = "3.14159"
converted_float_from_str = float(val_str_to_float)
print(f"string '{val_str_to_float}' to float: {converted_float_from_str}", type(converted_float_from_str))

# 5.3 str() - 转换为字符串
val_int_to_str = 500
converted_str_from_int = str(val_int_to_str)
print(f"int {val_int_to_str} to str: '{converted_str_from_int}'", type(converted_str_from_int))

val_float_to_str = 98.6
converted_str_from_float = str(val_float_to_str)
print(f"float {val_float_to_str} to str: '{converted_str_from_float}'", type(converted_str_from_float))

val_bool_to_str = True
converted_str_from_bool = str(val_bool_to_str)
print(f"bool {val_bool_to_str} to str: '{converted_str_from_bool}'", type(converted_str_from_bool))

# 5.4 bool() - 转换为布尔型
# 数值类型：0, 0.0 为 False，其他为 True
print("bool(0):", bool(0))         # False
print("bool(123):", bool(123))       # True
print("bool(-1):", bool(-1))        # True
print("bool(0.0):", bool(0.0))       # False
print("bool(3.14):", bool(3.14))     # True

# 字符串类型：空字符串 "" 为 False，其他为 True
print("bool(''):", bool(''))        # False
print("bool('hello'):", bool('hello')) # True
print("bool('False'):", bool('False')) # True (因为是非空字符串)

# None类型转换为布尔型是False
print("bool(None):", bool(None))     # False

# 5.5 chr() - 整数转对应编码的字符
ascii_code = 65 # 大写字母 'A' 的 ASCII 码
character_A = chr(ascii_code)
print(f"chr({ascii_code}): '{character_A}'", type(character_A))

unicode_val = 9731 # 雪人 '☃' 的 Unicode 码
char_snowman = chr(unicode_val)
print(f"chr({unicode_val}): '{char_snowman}'", type(char_snowman))

# 5.6 ord() - 字符转对应编码的整数
char_B = 'B'
ascii_val_B = ord(char_B)
print(f"ord('{char_B}'): {ascii_val_B}", type(ascii_val_B))

char_sigma = 'Σ' # 希腊字母 Sigma
unicode_val_sigma = ord(char_sigma)
print(f"ord('{char_sigma}'): {unicode_val_sigma}", type(unicode_val_sigma))

# -----------------------------------------------------------------------------
# 总结：
# - 使用变量保存数据。
# - 变量有不同类型：int, float, str, bool 等。
# - 遵守变量命名规则和惯例。
# - 可以使用内置函数进行类型转换。
# -----------------------------------------------------------------------------

print("\n--- End of Day 03 Variables Demo ---")