## 一、迭代器 (Iterator)

### 1. 核心概念

- **迭代 (Iteration)**: 访问集合（如列表、元组、字符串、字典、集合等）中元素的一种方式。
    
- **可迭代对象 (Iterable)**: 能够提供迭代器的对象。如果一个对象实现了 __iter__() 方法，那么它就是可迭代的。常见的可迭代对象有列表、元组、字符串、字典、集合、文件对象等。
    
- **迭代器 (Iterator)**:
    
    - 一个可以记住遍历位置的对象。
        
    - 只能**向前**遍历，不能后退。
        
    - 实现了 __iter__() 和 __next__() 两个核心方法 (迭代器协议)。
        
        - __iter__(): 返回迭代器对象自身。
            
        - __next__(): 返回序列中的下一个元素。当没有更多元素时，引发 StopIteration 异常。
            

### 2. 使用迭代器

- **iter(iterable)**: 内置函数，接收一个可迭代对象作为参数，返回其对应的迭代器。
    
- **next(iterator)**: 内置函数，接收一个迭代器作为参数，返回其下一个元素。
    

```python
my_list = [10, 20, 30]
my_iterator = iter(my_list) # 获取列表的迭代器

print(next(my_iterator))  # 10
print(next(my_iterator))  # 20
# print(next(my_iterator))  # 30
# print(next(my_iterator))  # StopIteration (因为没有更多元素了)
```



### 3. for 循环与迭代器

for 循环在后台自动处理迭代过程：

1. 调用可迭代对象的 __iter__() 方法获取迭代器。
    
2. 重复调用迭代器的 __next__() 方法获取下一个元素。
    
3. 当 __next__() 引发 StopIteration 异常时，循环自动终止。
    

```python
for item in my_list: # my_list 是可迭代的
    print(item)
```



### 4. 创建自定义迭代器类

类需要实现 __iter__() 和 __next__() 方法。

```python
class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self # 迭代器对象是自身

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current -1 # 返回0, 1, ..., limit-1
        else:
            raise StopIteration

counter = CountUpTo(3)
for num in counter:
    print(num) # 0, 1, 2
```

### 5. StopIteration 异常

用于标识迭代的完成。__next__() 方法在没有更多元素可返回时必须引发此异常。

## 二、生成器 (Generator)

### 1. 核心概念

- **生成器函数**: 任何包含 yield 关键字的Python函数。
    
- **yield 关键字**:
    
    - 当函数执行到 yield 语句时，函数会**暂停**执行，并将 yield 后面的表达式的值作为当前迭代的产出返回给调用者。
        
    - 函数的状态（包括局部变量、指令指针等）会被保存。
        
    - 当再次调用生成器对象的 next() 方法（或在 for 循环中迭代）时，函数会从上次暂停的地方**恢复**执行，直到遇到下一个 yield 或函数结束。
        
- **生成器对象**: 调用生成器函数时，它并**不立即执行函数体**，而是返回一个**生成器对象**。生成器对象是一种特殊的迭代器，自动实现了迭代器协议 (__iter__() 和 __next__())。
    
- **优势**:
    
    - **按需生成 (Lazy Evaluation)**: 值是在迭代过程中逐个产生的，而不是一次性计算并存储所有值。
        
    - **内存高效**: 对于可能产生大量数据的序列，生成器能极大地节省内存。
        
    - **代码简洁**: 通常比手动实现迭代器类更简洁。
        

### 2. 创建和使用生成器

```python
def simple_generator(n):
    print("Generator started")
    count = 0
    while count < n:
        print(f"Yielding {count}")
        yield count # 产出值并暂停
        count += 1
        print("Generator resumed")
    print("Generator finished")

gen = simple_generator(3) # 创建生成器对象，函数体未执行
print(type(gen))          # <class 'generator'>

print(next(gen)) # 输出: Generator started, Yielding 0, 返回 0
print(next(gen)) # 输出: Generator resumed, Yielding 1, 返回 1
# ...
# for value in gen: # 也可以用for循环迭代
#     print(value)
```



### 3. 示例：斐波那契数列生成器

```python
def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci_gen(10): # 获取前10个斐波那契数
    print(num, end=" ") # 0 1 1 2 3 5 8 13 21 34
```


### 4. 生成器表达式 (Generator Expressions)

- 一种简洁的创建生成器对象的方式，语法类似列表生成式，但使用圆括号 ()。
    
- 不立即计算所有值，而是返回一个生成器对象。
    
- 语法: (expression for item in iterable if condition)
    

```python
squares_gen = (x**2 for x in range(5)) # 创建生成器对象
# print(type(squares_gen)) # <class 'generator'>
for square in squares_gen:
    print(square) # 0, 1, 4, 9, 16
```


## 总结

- **迭代器**是Python中实现迭代访问序列元素的基础机制，遵循迭代器协议 (__iter__ 和 __next__)。
    
- **生成器**是一种特殊的迭代器，通过 yield 关键字使函数能够按需、逐个地产生值，非常适合处理大数据流或无限序列，且代码通常更简洁。
    
- 理解迭代器和生成器有助于编写更高效、更Pythonic的代码，尤其是在处理数据序列和自定义迭代行为时。