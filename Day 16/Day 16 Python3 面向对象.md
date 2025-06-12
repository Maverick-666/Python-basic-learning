## 核心概念

- **类 (Class)**: 对象的蓝图或模板，定义了对象的共同属性和方法。
    
- **对象 (Object/Instance)**: 类的具体化实例。每个对象拥有类定义的属性和方法。
    
- **封装 (Encapsulation)**: 将数据（属性）和操作数据的方法（函数）捆绑在一起（即在类中）。
    
- **继承 (Inheritance)**: 子类可以继承父类的属性和方法，实现代码复用和层级关系。
    
- **多态 (Polymorphism)**: 不同类的对象可以响应相同的方法调用，但表现出各自的行为。
    

## 一、类定义与实例化

### 1. 基本语法

```python
class ClassName:
    # 类变量 (所有实例共享)
    class_attr = "I am a class attribute"

    # 构造方法 (初始化实例)
    def __init__(self, param1, param2):
        print(f"{ClassName.__name__} instance created.")
        # 实例变量 (每个实例独有)
        self.instance_attr1 = param1
        self.instance_attr2 = param2

    # 实例方法 (操作实例数据)
    def instance_method(self):
        return f"Attr1: {self.instance_attr1}, Attr2: {self.instance_attr2}"

# 实例化：创建一个类的对象
my_object = ClassName("value1", "value2")
```


### 2. __init__ 方法 (构造方法/初始化器)

- 在创建类的实例时自动调用。
    
- 第一个参数通常是 self，代表实例本身。
    
- 用于初始化实例的属性 (实例变量)。
    
- 可以接受参数，在实例化时传递。
    

### 3. self 参数

- 类中定义的方法的第一个参数**必须**是 self (惯例名称)。
    
- self 指向调用该方法的实例对象。
    
- 通过 self 可以访问实例的属性 (self.attribute_name) 和调用其他实例方法 (self.method_name())。
    
- self 不是Python关键字，但强烈建议遵循此惯例。
    

### 4. 访问属性和方法

使用点 . 操作符：

- object_name.attribute_name
    
- object_name.method_name()
    
- ClassName.class_attribute_name (通过类名访问类变量)
    

```python
print(my_object.pythoninstance_attr1) # "value1"
print(my_object.instance_method())
print(ClassName.class_attr)
```


## 二、继承 (Inheritance)

### 1. 单继承

子类（派生类）继承一个父类（基类）的属性和方法。

```python
class Parent:
    parent_attr = "I am from Parent"
    def __init__(self):
        self.parent_init_attr = "Parent Initialized"
    def parent_method(self):
        return "Method from Parent"

class Child(Parent): # Child 继承自 Parent
    def __init__(self):
        super().__init__() # 调用父类的 __init__ (推荐方式)
        # Parent.__init__(self) # 也可以这样调用，但 super() 更灵活
        self.child_attr = "I am from Child"
    def child_method(self):
        return "Method from Child"

my_child = Child()
print(my_child.parent_attr)       # "I am from Parent" (继承的类属性)
print(my_child.parent_init_attr)  # "Parent Initialized" (通过super()调用父类__init__)
print(my_child.parent_method())   # "Method from Parent" (继承的方法)
print(my_child.child_attr)        # "I am from Child"
print(my_child.child_method())    # "Method from Child"
```



- **super()**: 内置函数，用于调用父类的方法，常用于在子类的 __init__ 中调用父类的 __init__，或在重写的方法中调用父类的同名方法。
    

### 2. 多继承

一个子类可以继承多个父类。

```python
class Base1:
    def method(self): return "Method from Base1"
class Base2:
    def method(self): return "Method from Base2" # 与Base1同名方法
    def another_method(self): return "Another from Base2"

class MultiDerived(Base1, Base2): # 继承顺序 Base1, Base2
    pass

obj_multi = MultiDerived()
print(obj_multi.method()) # "Method from Base1" (按MRO顺序，Base1在前)
print(obj_multi.another_method()) # "Another from Base2"
```



- **方法解析顺序 (MRO - Method Resolution Order)**: Python 使用C3线性化算法确定在多继承中查找方法的顺序。通常是从左到右查找父类。可以通过 ClassName.mro() 或 ClassName.__mro__ 查看。
    

### 3. 方法重写 (Overriding)

子类可以重新定义父类中已有的方法，以实现特定的行为。

```python
class Animal:
    def speak(self): return "Generic animal sound"

class Dog(Animal):
    def speak(self): # 重写父类的 speak 方法
        return "Woof!"

my_dog = Dog()
print(my_dog.speak()) # "Woof!" (调用的是Dog类中重写的方法)
# 调用被重写的父类方法: super().speak()
```


## 三、类的属性与方法细节

### 1. 类变量 vs 实例变量

- **类变量**: 定义在类中、方法之外。被所有实例共享。通过类名或实例名访问 (如果实例没有同名实例变量覆盖)。
    
- **实例变量**: 通常在 __init__ 方法中通过 self.variable = value 定义。每个实例独有一份。
    

### 2. 私有属性和方法 (Name Mangling)

- 以**双下划线 __ 开头**（且末尾没有或最多一个下划线）的属性或方法名 (如 __private_attr, __private_method()) 会被Python进行**名称重整 (name mangling)**。
    
- 它们会被重命名为 _ClassName__memberName。
    
- **目的**: 避免子类意外覆盖父类的私有成员，并非实现严格的私有性（仍可通过重整后的名称访问）。
    

```python
class MySecret:
    def __init__(self):
        self.__secret = "top secret" # 会被重整为 _MySecret__secret
    def get_secret(self):
        return self.__secret

secret_obj = MySecret()
# print(secret_obj.__secret) # AttributeError
print(secret_obj._MySecret__secret) # 可以访问，但不推荐
```

### 3. 类的专有方法 (Special/Magic/Dunder Methods)

- 以双下划线开头和结尾的方法，如 __init__, __str__, __len__, __add__等。
    
- Python在执行特定操作时会自动调用这些方法，允许我们自定义类的行为。
    
    - __str__(self): 当 print(obj) 或 str(obj) 时调用，应返回一个用户友好的字符串表示。
        
    - __repr__(self): 当 repr(obj) 时调用，或在交互式解释器中直接输入对象名时，应返回一个明确的、最好能重现对象的字符串表示。
        
    - __len__(self): 当 len(obj) 时调用。
        
    - __add__(self, other): 当 obj1 + obj2 时调用 (运算符重载)。
        
    - 还有许多其他专有方法用于实现比较、属性访问、迭代等。
        

### 4. 运算符重载

通过实现特定的专有方法，可以使自定义类的对象支持标准的Python运算符。

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __str__(self): return f"({self.x}, {self.y})"
    def __add__(self, other): # 重载 + 运算符
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2 # 调用 p1.__add__(p2)
print(p3) # (4, 6) (调用 p3.__str__())
```



## 总结

- 面向对象编程通过类和对象来组织代码，模拟现实世界或抽象概念。
    
- 封装、继承和多态是OOP的核心特性，有助于构建模块化、可复用、可扩展的软件。
    
- Python的类机制简洁而强大，self参数、__init__构造器、super()、私有成员名称重整以及丰富的专有方法是其重要组成部分。
    
- 理解MRO对于正确使用多继承至关重要。