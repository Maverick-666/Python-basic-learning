# 第1题
"""
类表示拥有共同特征，共同方法的一群对象
对象则是拥有类特征的个体，是具体的实例
"""
# 第2题
"""
__init__()方法在面向对象编程中通常扮演什么角色:初始化实例
它在什么时候被自动调用？ 创建对象的时候
"""
# 第3题
"""
类变量相当于默认值，对于所有实例都有效，作用域是类
而实例变量只是他自身的值
如果一个实例修改了其继承自类的同名变量，则变量会被覆盖成修改后的值，但是对于其他实例没有影响
"""
# 第4题
"""
果一个Dog类继承自Animal类，那么实例可以访问Animal类的所有特征比如self.name等以及方法，可以用super方法访问
"""
# 第5题
"""
super().__init__()相当于调用父类的构造方法来初始化继承的属性
"""
# 第6题
"""
方法重写就是在继承父类的方法时，对他进行修改，修改成属于子类的方法
如果想用父类的那个原始方法，要在方法内使用super().方法
"""
# 第7题
"""
class C(A, B):
先调用A，如果A找不到那么就一直找A的父类，直到找到自己本身就是父类，再调用B
"""
# 第8题
"""
在属性前面添加"__"
Python 会进行名称重整变为 _ClassName__secretCount。
目的是避免子类意外覆盖，并非严格的私有
"""
# 第9题
"""
会直接调用str()方法下return的值
"""
# 第10题
"""
add()方法
"""
# 第11题
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title:{self.title}, Author:{self.author}")

book1 = Book("Python", "Maverick")
book1.display_info()

# 第12题
class Ebook(Book):

    def __init__(self, title, author,file_format):
        super().__init__(title, author)
        self.file_format = file_format

    def display_info(self):
        print(f"Title:{self.title}, Author:{self.author}, File Format:{self.file_format}")

ebook1 = Ebook("Python", "Maverick",file_format="PDF")
ebook1.display_info()

# 第13题
"""
这意味着Python信任其用户能够负责任地使用代码，而不是强制实行严格的不可绕过的访问控制规则
"""
# 第14题
"""
这种现象体现了面向对象编程中的多态性（。多态性允许不同类的对象通过相同的接口调用表现出不同的行为。
"""
# 第15题
"""
__str__()：面向最终用户   设计目的：提供一个可读性强、友好、简洁的字符串表示，便于用户理解当前对象的内容

__repr__()：面向开发者  设计目的：提供一个明确、无歧义、通常完整的对象信息
"""
