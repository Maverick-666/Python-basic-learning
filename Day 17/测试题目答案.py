# 第1题
"""
语法错误是指语句的语法没有遵循规定，例如缩进之类，这些错误很容易排查
异常是指程序运行时遇到的错误，但是在此之前要保证语法正确
"""
# 第2题
"""
在一个try块执行时，如果发生了异常，程序将停止在try中的执行，转而执行except语句中的错误处理
try块没有异常的时候，程序不会运行except中的语句，直至try运行完
"""
# 第3题
"""
按照顺序从上往下，按照异常匹配
同时匹配多个优先触发排在前面的except
"""
# 第4题
"""
else语句会在try块没有发生异常的时候执行
else子句相对于将所有代码都放在try块中: 对于想要调试部分的代码，可以一条一条try，确定没问题的可以放在else里
这样缩小了排查的范围
"""
# 第5题
"""
finally 主要目的是确保文件，网络的安全，比如一个文件以写入格式打开，写入的格式是10/0，显然会触发不能除以0的错误
但是finally语句仍然可以在有except没有提到该错误的时候将文件关闭
"""
# 第6题
"""
raise 语句的作用是当遇到某个情况时主动抛出错误
例子：
if received_data < 0: raise ValueError("不能小于0")
"""
# 第7题
"""
重新抛出最近一次被捕获的异常(但我不知道这么做的目的是为什么)
"""
# 第8题
"""
因为即使python存在很多异常，在项目开发阶段，有一些跟数据大小，包括特殊情况的“问题”即使程序认定是正确，但是程序员不想得到这个结果
就可以自定义异常；需要继承exception
"""
# 第9题
"""
预定义：exit()
with open("myfile.txt")as f:这样的语句确保了文件一定会被关闭
"""
# 第10题
"""
assert语句主要用途是提出断言，在开发阶段用来预判错误
在语句为false的时候会触发
 python -O xx.py会禁用
"""
# 第11题
"""
非常具体的异常的优点是修改目标非常明确，能够直接知道是哪个地方出错了   缺点是：如果需要处理多种不同类型的异常，可能会导致 try/except 块变得复杂且冗长
捕获一个非常通用的异常，可以通过type(Exception).__name__的方式查找出来 缺点是能会无意间捕获并处理了不应被处理的异常，比如编程错误（如 TypeError, IndexError 等），从而掩盖了潜在的问题。
"""
# 第12题
"""
ve指的是ValueError，我们可以在语句后面加上括号，用来返回具体的数值上的问题
"""
# 第13题
"""
会traceback到错误的那一行，然后指出是什么类型的错误
"""
# 第14题
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return result
    finally:
        print("Division attempt finished.")
# 第15题
class InvalidUsernameError(Exception):

    def __init__(self,message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

def register_user(username):
    if len(username) < 5:
        raise InvalidUsernameError(f"Username must be at least 5 characters long.")

try: # 需要 try-except 来捕获并打印
        register_user("bob")
except InvalidUsernameError as e:
        print(e)






