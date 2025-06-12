# 第一题
"""
什么是表达式？ 表达式是含变量和参数的运算式，可以有多种运算
例子：
1、
a = 2+3*5, b = 2*3+5 两者不同
2、
c = 10
c = c*10 +20
c *= 10 + 20
c += 10*20 这三个是不同的值
"""

# 第二题
a = 17
b = 5
c = a//b # c是3，是整除的意思
d = a%b # d是2，是除余的意思

# 第三题
s = 2**10
s1 = pow(2,10)

# 第四题
count = 5
count *= 3
# 现在他是15

# 第五题
"""
海象运算符：让赋值和变量自身在同一个式子中
"""
if a:= 2 ==2:
    print(a:=3)
#结果会输出三，因为a:= 2 ==2的意思是在赋2给a的同时a也是作为一个变量去做“==”运算
#最后输出的是重新赋值3给a,输出的print也是输出变量a，也就是重新赋值过的
"""
反馈：
作用描述基本正确，它允许在表达式内部进行赋值。
您的示例代码 (a:= 2 == 2) 是有问题的。海象运算符的正确用法是 (a := expression_value)。
a := 2 == 2 会将 2 == 2 (即 True) 赋值给 a。所以 if (a := (2 == 2)) 相当于 if True:。
然后 print(a:=3)，a 被重新赋值为 3，并打印 3。
一个更典型的例子是：
my_list = [1, 2, 3, 4, 5]
if (n := len(my_list)) > 3:
    print(f"The list has {n} elements, which is more than 3.")
# n 在 if 语句结束后仍然可用

"""

# 第六题
"""
== 是判断值
而is在判断值的同时还要判断内存地址
a = 1
b = 1
a == b 返回 true
a is b 返回 false
"""

# 第七题
"""
3<5<7 返回true是肯定的

"""

# 第八题
#print(10/0 and 5>3)
"""
python会报错，不能除以0
如果能避免错误，那也是false
因为10/0是错误，而5>3正确，但是and取True当且仅当前后同真
"""
x = 0
# (x != 0) and (10 / x > 1)  # 如果 x 是 0，这里会报错
# 更安全的写法，利用短路
if x != 0 and (10 / x > 1): # 因为 x!=0 是 False, (10/x > 1) 不会被执行
    print("Condition met")
else:
    print("Condition not met or x is zero") # 会输出这个

# 第九题
"""
x or y  True
not x   False
not (x or y)   False
"""

# 第十题
"""
我不太确定，但我猜是比较True和False的时候

反馈# 比较 True、False 是一种情况。更经典和重要的场景是比较 None。
"""

# 第十一题
"""
"pro" in s  True
"java" not in s True
"python" in L False
20 in L True
"""

# 第十二题
num1 = 12 # 1100
num2 = 10 # 1010
# num1 & num2 按位与是 1000 十进制是8

# 第十三题
# 假设加速度是float，时间是int，单位是min
a = float(input("请输入加速度"))
t = int(input("请输入用时（min）"))
s = 0.5 * a * (t ** 2)
print(f'所用的时间是{s:.2f}')

# 第十四题
chinese_score = 100
math_score = 50
total_score = chinese_score + math_score
if((chinese_score >=60 and math_score >= 60) or total_score>=150):
    print("通过！")


# 第十五题
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")