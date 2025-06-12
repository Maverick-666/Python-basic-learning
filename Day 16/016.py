# day_18_oop_basics.py

# -----------------------------------------------------------------------------
# 面向对象编程 (OOP) 简介
# - 类 (Class): 描述具有相同属性和方法的对象的集合 (蓝图)。
# - 对象 (Object/Instance): 类的具体实例。
# - 方法 (Method): 类中定义的函数，通常第一个参数是 self。
# - 属性 (Attribute):
#   - 类变量 (Class Variable): 类所有实例共享的变量，定义在类中方法外。
#   - 实例变量 (Instance Variable): 每个实例独有的变量，通常在 __init__ 中通过 self.variable_name 定义。
# - 继承 (Inheritance): 子类继承父类的属性和方法。
# - 实例化 (Instantiation): 创建一个类的实例的过程。
# - 方法重写 (Override): 子类重新定义父类中已有的方法。
# -----------------------------------------------------------------------------

# --- 1. 类定义 (Class Definition) ---
print("--- 1. 类定义与实例化 ---")
class MyFirstClass:
    """一个简单的类实例 - MyFirstClass"""
    class_variable_i = 12345  # 类变量

    def __init__(self, instance_value=0): # 构造方法 (initializer)
        print("MyFirstClass __init__ called.")
        self.instance_variable_data = [instance_value] # 实例变量

    def instance_method_f(self): # 实例方法
        """一个简单的实例方法"""
        return f'hello world from instance, data: {self.instance_variable_data}'

# --- 2. 类对象操作 ---
# 2.1 属性引用 (访问类变量)
print(f"Accessing class variable via class: MyFirstClass.class_variable_i = {MyFirstClass.class_variable_i}")

# 2.2 实例化 (Creating an instance / object)
# 实例化类时，__init__ 方法会自动调用
x_instance = MyFirstClass(100) # 创建 MyFirstClass 的一个实例，传入 instance_value
print(f"Type of x_instance: {type(x_instance)}")

# 访问实例的属性和方法
print(f"Accessing instance variable via instance: x_instance.instance_variable_data = {x_instance.instance_variable_data}")
print(f"Accessing class variable via instance: x_instance.class_variable_i = {x_instance.class_variable_i}") # 实例可以访问类变量
print(f"Calling instance method: x_instance.instance_method_f() returns '{x_instance.instance_method_f()}'")

# 修改实例变量
x_instance.instance_variable_data.append(200)
print(f"x_instance.instance_variable_data after modification: {x_instance.instance_variable_data}")

# 修改类变量 (通过类名修改会影响所有实例，如果实例没有同名实例变量覆盖它)
MyFirstClass.class_variable_i = 54321
y_instance = MyFirstClass(300)
print(f"y_instance.class_variable_i after class var change: {y_instance.class_variable_i}") # 54321
print(f"x_instance.class_variable_i after class var change: {x_instance.class_variable_i}") # 54321

# 如果实例创建同名实例变量，会覆盖类变量的访问
x_instance.class_variable_i = 777 # x_instance 现在有了自己的 class_variable_i 实例变量
print(f"x_instance.class_variable_i after instance assignment: {x_instance.class_variable_i}") # 777
print(f"y_instance.class_variable_i (unaffected): {y_instance.class_variable_i}")             # 54321
print(f"MyFirstClass.class_variable_i (class var): {MyFirstClass.class_variable_i}")      # 54321
print("\n")

# --- 3. __init__ 方法 (构造方法) ---
print("--- 3. __init__ 方法 ---")
class ComplexNumber:
    def __init__(self, realpart, imagpart): # 构造方法可以有参数
        print(f"ComplexNumber __init__ called for ({realpart}, {imagpart}i)")
        self.r = realpart # 实例变量 r
        self.i = imagpart # 实例变量 i

z = ComplexNumber(3.0, -4.5) # 实例化时传递参数给 __init__
print(f"Complex number z: real part = {z.r}, imaginary part = {z.i}")
print("\n")

# --- 4. self 参数 ---
# - 类的方法的第一个参数通常是 self (惯例)。
# - self 代表类的实例本身，允许方法访问实例的属性和调用其他实例方法。
# - self 不是关键字，但强烈建议使用。
print("--- 4. self 参数 ---")
class TestSelf:
    def print_self_info(self_param_name): # 第一个参数是实例引用
        print(f"Inside print_self_info:")
        print(f"  self (or equivalent parameter) is: {self_param_name}")
        print(f"  Type of self: {type(self_param_name)}")
        print(f"  self.__class__ is: {self_param_name.__class__}") # 指向类本身

test_obj = TestSelf()
test_obj.print_self_info() # Python 自动将 test_obj 作为第一个参数传递
print("\n")

# --- 5. 类的方法 (Instance Methods) ---
print("--- 5. 类的方法 ---")
class People:
    # 类变量 (会被实例共享，除非实例有同名实例变量)
    # name = '' # 通常不在类级别定义可变的实例状态
    # age = 0
    # __weight = 0 # 私有类变量 (不推荐这样用，通常实例变量在 __init__ 中定义)

    def __init__(self, n, a, w): # 构造方法，初始化实例变量
        self.name = n       # 实例变量
        self.age = a        # 实例变量
        self.__weight = w   # 私有实例变量 (name mangling: _People__weight)

    def speak(self): # 实例方法
        print(f"{self.name} 说: 我 {self.age} 岁, 体重 (保密) {self.__weight}kg.")

    def get_weight(self): # 提供一个方法来访问私有属性
        return self.__weight

person_instance = People('张三', 30, 70)
person_instance.speak()
print(f"{person_instance.name} 的体重是: {person_instance.get_weight()}kg")
# print(person_instance.__weight) # AttributeError: 'People' object has no attribute '__weight'
# 可以通过名称重整访问 (不推荐直接访问): print(person_instance._People__weight)
print("\n")

# --- 6. 继承 (Inheritance) ---
print("--- 6. 继承 ---")
# class DerivedClassName(BaseClassName):
# class DerivedClassName(module_name.BaseClassName):

# 6.1 单继承
class Student(People): # Student 继承自 People
    def __init__(self, n, a, w, g):
        # 调用父类的构造方法来初始化继承的属性
        super().__init__(n, a, w) # 推荐使用 super()
        # People.__init__(self, n, a, w) # 也可以直接调用父类__init__，但需传入self
        self.grade = g # 子类新增的实例变量

    # 方法重写 (Override)
    def speak(self):
        # 调用父类被重写的方法 (可选)
        # super().speak() # 如果需要父类的行为
        print(f"{self.name} 说: 我 {self.age} 岁了，我在读 {self.grade} 年级。体重依然是 {self.get_weight()}kg.")

student_instance = Student('李四', 10, 40, 3)
student_instance.speak()
print("\n")

# 6.2 多继承
# class DerivedClassName(Base1, Base2, Base3):
# 方法解析顺序 (MRO - Method Resolution Order): 从左到右查找父类。
print("--- 6.2 多继承 ---")
class Speaker:
    def __init__(self, speaker_name, topic):
        print("Speaker __init__ called.")
        self.speaker_name = speaker_name # 注意：可能与Student的name冲突
        self.topic = topic

    def speak(self): # 与 People 和 Student 中的 speak 方法同名
        print(f"我叫 {self.speaker_name}，我是一个演说家，我演讲的主题是 {self.topic}")

class SampleMultiInheritance(Student, Speaker): # 继承顺序：Student, Speaker
    def __init__(self, n, a, w, g, t):
        print("SampleMultiInheritance __init__ called.")
        # 需要分别调用父类的 __init__
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t) # Speaker的speaker_name会覆盖Student的name (如果都用self.name)
                                     # 为避免冲突，Speaker中用了self.speaker_name

    # 如果不重写 speak, 则会调用 Student 的 speak (MRO: Sample -> Student -> People -> Speaker -> object)
    # 但由于 Speaker 在 Student 之后，且 Student 重写了 People.speak,
    # 如果 Sample 不重写，会用 Student.speak。
    # 如果 Student 没有 speak，会用 People.speak。
    # 如果 People 也没有 speak，才会用 Speaker.speak。
    # 原文例子中，是 class sample(speaker,student)，所以 speaker 的 speak 优先。
    # 我们这里用 class sample(Student, Speaker)，所以 Student 的 speak 优先。

class SampleMultiInheritanceOriginal(Speaker, Student): # 按原文顺序
     def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)

print("--- MRO for SampleMultiInheritance (Student, Speaker) ---")
print(SampleMultiInheritance.mro())
multi_inherit_obj = SampleMultiInheritance("王五", 25, 70, 1, "Python高级特性")
multi_inherit_obj.speak() # 会调用 Student 的 speak 方法

print("\n--- MRO for SampleMultiInheritanceOriginal (Speaker, Student) ---")
print(SampleMultiInheritanceOriginal.mro())
multi_inherit_obj_orig = SampleMultiInheritanceOriginal("赵六", 20, 60, 2, "数据科学")
multi_inherit_obj_orig.speak() # 会调用 Speaker 的 speak 方法
print("\n")


# --- 7. 方法重写 (Method Overriding) ---
# (已在 Student 类中演示 speak 方法的重写)
print("--- 7. 方法重写 ---")
class Parent:
   def myMethod(self):
      print ('调用父类方法 (Parent.myMethod)')

class Child(Parent):
   def myMethod(self): # 重写父类的 myMethod
      print ('调用子类方法 (Child.myMethod)')

child_obj = Child()
child_obj.myMethod()        # 调用子类重写后的方法

# 使用 super() 调用父类被覆盖的方法
class ChildWithSuper(Parent):
    def myMethod(self):
        print("ChildWithSuper: Calling super's method first.")
        super().myMethod() # 调用父类 Parent 的 myMethod
        print("ChildWithSuper: After calling super's method.")

child_super_obj = ChildWithSuper()
child_super_obj.myMethod()
print("\n")

# --- 8. 类属性与方法 ---
# 8.1 类的私有属性 (__private_attrs)
# - 双下划线开头 (如 __secretCount)。
# - Python 会进行名称重整 (name mangling) 变为 _ClassName__secretCount。
# - 目的是避免子类意外覆盖，并非严格的私有。
print("--- 8.1 类的私有属性 ---")
class JustCounter:
    __secretCount = 0  # 私有类变量 (实际上是 _JustCounter__secretCount)
    publicCount = 0    # 公开类变量

    def count(self):
        JustCounter.__secretCount += 1 # 访问私有类变量
        self.publicCount += 1          # 访问公开类变量 (或创建实例变量)
        print(f"  Inside count: __secretCount = {JustCounter.__secretCount}")

counter_obj1 = JustCounter()
counter_obj1.count() # __secretCount=1, publicCount=1
counter_obj2 = JustCounter()
counter_obj2.count() # __secretCount=2, publicCount=1 (publicCount是实例变量了)
                     # 如果想让 publicCount 也是类共享的，应使用 JustCounter.publicCount

print(f"counter_obj1.publicCount: {counter_obj1.publicCount}")
# print(counter_obj1.__secretCount) # AttributeError: 'JustCounter' object has no attribute '__secretCount'
# 可以通过名称重整访问 (不推荐)
print(f"Accessing mangled name: counter_obj1._JustCounter__secretCount = {counter_obj1._JustCounter__secretCount}")

# 8.2 类的私有方法 (__private_method)
# - 双下划线开头。
# - 同样会进行名称重整。
# - 只能在类的内部通过 self.__private_method() (实际是 self._ClassName__private_method()) 调用。
print("\n--- 8.2 类的私有方法 ---")
class Site:
    def __init__(self, name, url):
        self.name = name       # public instance variable
        self.__url = url       # private instance variable

    def who(self):
        print(f'name  : {self.name}')
        print(f'url (private access): {self.__url}') # 内部访问私有属性

    def __internal_foo(self): # 私有方法
        print('这是私有方法 (__internal_foo) 执行')

    def public_foo(self):     # 公共方法
        print('这是公共方法 (public_foo) 执行, 将调用私有方法')
        self.__internal_foo() # 内部调用私有方法

site_obj = Site('教程网', 'www.example.com')
site_obj.who()
site_obj.public_foo()
# site_obj.__internal_foo() # AttributeError
# 可以通过名称重整访问 (不推荐)
# site_obj._Site__internal_foo()
print("\n")

# --- 9. 类的专有方法 (Special/Magic/Dunder Methods) ---
# - 以双下划线开头和结尾 (e.g., __init__, __str__, __len__, __add__)。
# - Python 在特定操作时会自动调用它们。
print("--- 9. 类的专有方法与运算符重载 ---")
class Vector:
   def __init__(self, a_coord, b_coord):
      self.a = a_coord
      self.b = b_coord
      print(f"Vector created with ({self.a}, {self.b})")

   def __str__(self): # 当 print(vector_obj) 或 str(vector_obj) 时调用
      return f'Vector ({self.a}, {self.b})'

   def __add__(self, other_vector): # 当 vector1 + vector2 时调用 (运算符重载)
      print(f"Adding {self} to {other_vector}")
      if isinstance(other_vector, Vector):
          return Vector(self.a + other_vector.a, self.b + other_vector.b)
      return NotImplemented # 表示此类型的加法未实现

   def __len__(self): # 当 len(vector_obj) 时调用
       # 示例：返回向量的维度 (这里是2) 或其他自定义长度
       return 2 # 或者 int( (self.a**2 + self.b**2)**0.5 ) 如果是求模长

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(f"String representation of v1: {v1}") # 调用 __str__
print(f"String representation of v2: {str(v2)}")

v_sum = v1 + v2 # 调用 __add__
print(f"Sum of v1 and v2: {v_sum}") # 调用新 Vector 的 __str__

print(f"Length of v1 (from __len__): {len(v1)}")
print("\n")

print("--- End of OOP Basics Demo ---")