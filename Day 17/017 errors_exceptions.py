# day_XX_errors_exceptions.py
import os
import sys # For sys.exc_info() and sys.exit()

# -----------------------------------------------------------------------------
# Python 错误和异常
# - 语法错误 (Syntax Errors / Parsing Errors): 程序开始运行前，Python解释器发现代码不符合语法规则。
# - 异常 (Exceptions): 程序语法正确，但在运行期间发生的错误。
# -----------------------------------------------------------------------------

# --- 1. 语法错误示例 (无法直接在脚本中运行，会导致解析失败) ---
# print "Hello, World!" # Python 3.x 中 print 是函数，这样写是语法错误
# if x > 0 y = x       # 缺少冒号是语法错误

# --- 2. 常见内置异常示例 (运行时会触发) ---
print("--- 2. 常见内置异常示例 ---")
try:
    # a_undefined_var # NameError: name 'a_undefined_var' is not defined
    # result = 10 / 0   # ZeroDivisionError: division by zero
    # my_list = [1, 2]
    # print(my_list[5]) # IndexError: list index out of range
    # my_dict = {'a': 1}
    # print(my_dict['b']) # KeyError: 'b'
    # int("abc")        # ValueError: invalid literal for int() with base 10: 'abc'
    # "hello" + 5     # TypeError: can only concatenate str (not "int") to str
    # import non_existent_module # ModuleNotFoundError: No module named 'non_existent_module'
    # open("non_existent_file.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory
    pass # 注释掉实际会引发异常的代码，以允许脚本继续执行
except Exception as e:
    print(f"Caught an expected exception during demo: {type(e).__name__} - {e}")


# -----------------------------------------------------------------------------
# 3. 异常处理 (Exception Handling)
# -----------------------------------------------------------------------------
print("\n--- 3. 异常处理 ---")

# --- 3.1 try / except ---
print("\n--- 3.1 try / except ---")
# 示例1: 用户输入整数
# while True: # 无限循环直到输入正确或中断 (在脚本演示中用有限次数)
for _ in range(2): # 尝试两次
    try:
        # x_input = int(input("请输入一个数字 (try/except): "))
        # 模拟输入以避免脚本暂停
        user_inputs = ["abc", "123"]
        if _ < len(user_inputs):
            current_input_sim = user_inputs[_]
            print(f"模拟输入: {current_input_sim}")
            x_input = int(current_input_sim)
            print(f"成功输入数字: {x_input}")
            break
        else: # 无法继续模拟
            break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
    except KeyboardInterrupt: # 用户按下 Ctrl+C
        print("\n用户中断了程序。")
        break # 退出循环

# 示例2: 处理多种特定异常和通用异常
print("\n--- 3.1.1 try / except (multiple specific and generic) ---")
try:
    # f_test = open('myfile.txt', 'r') # 可能引发 FileNotFoundError/OSError
    # s_test = f_test.readline()
    # i_test = int(s_test.strip())   # 可能引发 ValueError
    # 模拟不同错误
    # raise OSError("Simulated OS error")
    # raise ValueError("Simulated Value error")
    raise NameError("Simulated NameError for generic catch") # 模拟一个未特定捕获的错误
except FileNotFoundError as fnf_err: # Python 3.3+ OSError是FileNotFoundError的基类
    print(f"File not found error: {fnf_err}")
except OSError as os_err: # 捕获OSError及其子类 (如FileNotFoundError)
    print(f"OS error: {os_err}")
except ValueError:
    print("Could not convert data to an integer.")
except (RuntimeError, TypeError, NameError) as specific_group_err: # 捕获元组中列出的多种异常
    print(f"Caught one of (RuntimeError, TypeError, NameError): {specific_group_err}")
except: # 捕获所有其他未被上面捕获的异常 (通常不推荐，除非有特定目的)
    print(f"An unexpected error occurred: {sys.exc_info()[0]}")
    # raise # 可以选择重新抛出异常，让上层处理或程序终止
finally:
    # f_test.close() # 如果文件成功打开，应该关闭，但这里f_test可能未定义
    print("Generic exception block's finally executed (if try was entered).")


# --- 3.2 try / except ... else ---
# else 子句在 try 子句没有发生任何异常时执行。
print("\n--- 3.2 try / except ... else ---")
# 模拟命令行参数
# mock_argv = ["script_name.py", "existing_file.txt", "non_existent.txt"]
mock_argv = ["script_name.py", "sample.txt"] # 使用之前创建的sample.txt
if not os.path.exists("sample.txt"): # 确保sample.txt存在
    with open("sample.txt", "w") as f_temp_sample: f_temp_sample.write("line1\nline2")

for arg_file in mock_argv[1:]: # 跳过脚本名
    try:
        f_else_test = open(arg_file, 'r', encoding='utf-8')
    except IOError: # FileNotFoundError 是 IOError (也是 OSError) 的子类
        print(f'Cannot open {arg_file}')
    else:
        # try块成功执行后才执行else块
        print(f'{arg_file} has {len(f_else_test.readlines())} lines')
        f_else_test.close() # 确保关闭文件

# 示例：函数调用中的异常传递
def this_fails():
    x_fail = 1 / 0 # ZeroDivisionError

print("\n--- Exception propagation from function call ---")
try:
    this_fails()
except ZeroDivisionError as err_prop:
    print(f'Handling run-time error from function: {err_prop}')


# --- 3.3 try ... finally ---
# finally 子句无论是否发生异常都会执行 (通常用于资源清理)。
print("\n--- 3.3 try ... finally ---")
try:
    # raise KeyboardInterrupt # 模拟一个异常
    print("In try block (try...finally)")
    # result_div = 10 / 0 # 模拟另一个异常
except ZeroDivisionError:
    print("Caught ZeroDivisionError in try...finally example.")
finally:
    print('Finally clause executed (always runs).')

# 复杂示例：try/except/else/finally
def complex_divide_example(x, y):
    print(f"\nDividing {x} by {y}:")
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Invalid types for division!")
    else:
        print(f"Result is {result}")
        return result # 仅在无异常时返回
    finally:
        print("Executing finally clause in complex_divide_example.")
    # 如果发生未捕获的异常或捕获后没有return, 函数可能返回None(隐式)

complex_divide_example(10, 2)
complex_divide_example(10, 0)
complex_divide_example("10", "2") # TypeError, 会被捕获
try:
    complex_divide_example(10, "s") # TypeError, 会被捕获
except TypeError as e: # 演示上层捕获
    print(f"Caught TypeError at a higher level for (10, 's'): {e}")


# -----------------------------------------------------------------------------
# 4. 抛出异常 (Raising Exceptions) - raise
# -----------------------------------------------------------------------------
print("\n--- 4. 抛出异常 (raise) ---")
try:
    x_raise = 10
    if x_raise > 5:
        raise Exception(f'x 不能大于 5。x 的值为: {x_raise}') # 抛出通用异常
except Exception as e_raise:
    print(f"Caught raised exception: {e_raise}")

# 重新抛出捕获的异常
try:
    raise NameError('Simulated HiThere')
except NameError:
    print('An exception flew by! Re-raising it...')
    # raise # 重新抛出最近一次被捕获的异常
    pass # 在演示中不重新抛出，避免脚本终止


# -----------------------------------------------------------------------------
# 5. 用户自定义异常 (User-defined Exceptions)
# - 通过创建新的异常类 (继承自 Exception 或其子类)。
# -----------------------------------------------------------------------------
print("\n--- 5. 用户自定义异常 ---")
class MyCustomError(Exception):
    """自定义错误基类"""
    def __init__(self, message, error_code=None):
        super().__init__(message) # 调用基类构造函数
        self.message = message
        self.error_code = error_code
    def __str__(self):
        if self.error_code:
            return f"MyCustomError (Code {self.error_code}): {self.message}"
        return f"MyCustomError: {self.message}"

class ValueTooSmallError(MyCustomError):
    """当输入值太小时抛出"""
    def __init__(self, value, threshold):
        message = f"Value {value} is too small, must be >= {threshold}."
        super().__init__(message, error_code=101)
        self.value = value
        self.threshold = threshold

class ValueTooLargeError(MyCustomError):
    """当输入值太大时抛出"""
    def __init__(self, value, threshold):
        message = f"Value {value} is too large, must be <= {threshold}."
        super().__init__(message, error_code=102)
        self.value = value
        self.threshold = threshold

def check_value_range(val, min_val=0, max_val=100):
    if val < min_val:
        raise ValueTooSmallError(val, min_val)
    if val > max_val:
        raise ValueTooLargeError(val, max_val)
    print(f"Value {val} is within range [{min_val}, {max_val}].")

try:
    check_value_range(50)
    check_value_range(-10)
except MyCustomError as mce: # 可以捕获基类或特定子类
    print(f"Caught custom error: {mce}")

try:
    check_value_range(200)
except ValueTooLargeError as vtle: # 捕获特定子类
    print(f"Caught specific custom error: {vtle}")
except MyCustomError as mce_generic: # 如果上面没捕获，这里会捕获
    print(f"Caught generic custom error: {mce_generic}")


# -----------------------------------------------------------------------------
# 6. 定义清理行为 (with 语句是预定义的清理行为)
# - finally 子句确保代码无论如何都会执行。
# - with 语句 (上下文管理器) 自动处理资源的获取和释放 (如文件关闭)。
# -----------------------------------------------------------------------------
print("\n--- 6. 定义清理行为 (with 语句) ---")
# (之前的 with open(...) 示例已经演示了这一点)
# with 语句确保文件 f 在代码块结束时总是会被关闭，即使在处理过程中发生错误。
try:
    with open("temp_cleanup.txt", "w") as f_cleanup:
        f_cleanup.write("This is for with statement demo.\n")
        # Simulate an error after opening and writing
        # result_cleanup = 10 / 0
    print("'temp_cleanup.txt' processed and closed by with statement.")
except ZeroDivisionError:
    print("Error occurred within 'with' block, but file was still closed.")
finally:
    # 清理演示文件
    if os.path.exists("temp_cleanup.txt"):
        os.remove("temp_cleanup.txt")
    if os.path.exists("sample.txt"): # 清理之前创建的sample.txt
        os.remove("sample.txt")


# -----------------------------------------------------------------------------
# 7. 断言 (Assert) - (原文提及，补充演示)
# - assert expression[, arguments]
# - 如果 expression 为 False，则引发 AssertionError。
# - 通常用于调试和检查不应发生的条件。
# - 可以通过 python -O main.py 优化执行时忽略断言。
# -----------------------------------------------------------------------------
print("\n--- 7. 断言 (assert) ---")
def process_positive_number(num):
    assert num > 0, f"Number must be positive, got {num}"
    print(f"Processing positive number: {num}")

try:
    process_positive_number(10)
    process_positive_number(-5) # 这会引发 AssertionError
except AssertionError as ae:
    print(f"AssertionError caught: {ae}")


print("\n--- End of Errors and Exceptions Demo ---")