# 第1题
"""
可迭代对象和迭代器之间的主要区别是：可迭代对象能够提供迭代器，迭代器是可以记住遍历位置的对象
如果一个对象实现了iter()方法，它就是可迭代对象（例如列表，字符串可遍历）
如果一个对象实现了iter()方法和next()方法，那么他就能成为迭代器,用iter(x)表示，x是可迭代对象
"""
# 第2题
"""
迭代器协议包含iter()和next()方法，
iter()返回迭代器对象自身
next()是返回序列中下一个元素
"""
# 第3题
"""
iter()函数的作用是创建一个迭代器，它接受可迭代类型的参数
next()函数返回序列中的下一个元素，传入的参数是迭代器，如果没有更多元素，会返回StopIteration异常
"""
# 第4题
"""
当使用for item in my_iterable:这样的循环时
python在每次循环的时候调用一次next(my_iterable)
"""
# 第5题
"""
StopIteration异常扮演了提示一个迭代器中没有更多元素的角色
引发它是为了提醒程序员和读者迭代结束或者报告错误
"""
# 第6题
"""
yield语句让一个普通的Python函数变成一个“生成器函数”
调用一个生成器函数不会立刻执行
它首先返回生成器函数本身
如图要调用，要使用next()方法
"""
# 第7题
"""
yield关键字的作用是暂停程序并返回yield的值
执行到yield语句的时候，函数会暂停并返回值
下一次执行从yield的下一条语句开始
"""
# 第8题
"""
生成器的优势在于：1、用户能一条一条接受数据，更简洁
2、对于大量数据的输出，可以有效节省内存
"""
# 第9题
my_generator = (x**3 for x in range(5))
for item in my_generator:
    print(item)
# 第10题
class MyRange:
    def __init__(self,n):
        self.current = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            x = self.current
            self.current += 1
            return x
        else:
            raise StopIteration

Myrange = MyRange(5)
for item in Myrange:
    print(item)
# 第11题
def even_numbers():
    num = 1
    while True:
        yield num*2
        num += 1

my_even_numbers = even_numbers()
for _ in range(5):
    print(next(my_even_numbers))

# 第12题
"""
我不懂，我希望你能帮我讲的详细一些，就用python可执行文件帮我补充到这一单元的文件中吧
"""
# 第13题
"""
生成器是特殊的迭代器
不是所有迭代器都是生成器
"""
# 第14题
"""
因为系统同时得到百万条数据会非常占内存
使用生成器可以在得到每个条目后把内存省下来处理下一个
"""
# 第15题
"""
我觉得当遇到需要重复使用这个迭代器的时候，或者这个迭代器需要实现比较复杂或特殊的功能的时候可以使用
其他简单情况下可以直接使用生成器表达式来进行生成
"""

# 补充我的思考：在做算法题目的时候，如果遇到时间复杂度比较高，能不能在中间使用生成器进行优化呢
