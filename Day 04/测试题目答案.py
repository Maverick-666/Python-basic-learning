# 第1题
"""
for-in循环适用于确定循环次数
while循环适用于达成某个条件
"""

# 第2题
"""
3,5,7,9
"""
# 第3题
"""
命名成"_"这样做更简洁，使变量不会混淆
"""
# 第4题
"""
1、在每次循环的时候要做判断，在循环体内部设置相关变量，使其达成某一条件时循环结束
2、在函数体内部可以设置一个break，在达成条件时退出循环
"""
# 第5题
"""
作用是退出当前循环
break只会跳出一层
"""
# 第6题
"""
作用是跳过当前循环，进入下一次循环
break直接终止，它是继续
"""
# 第7题
"""
6次，2x3=6
"""
# 第8题
for i in range(5,0,-1):
    print(i)
# 第9题
n = 1
sum1 = 0
while n < 21:

    if n % 2 != 0:
        sum1 += n
    n += 1
print(f"{sum1}")

# 第10题
import random
lst = []
for _ in range(20):
    lst.append(random.randint(1,50))
lst1 = [r for r in lst if r % 2 == 0 ]
for i in lst1:
    if i > 20:
        print(f"找到了！是{i}")
        break
    else:
        continue
# 第11题
for j in range(1,11):
    if j!=5 and j!=7:
        print(j)

# 第12题
"""
正常结束就是执行
break结束就是不执行
"""
# 第13题
"""
假设要求24，32的最大公因数
先令a = 24,b =32
执行操作以后得到a=32,b=24显然大小没有影响
继续下一步a=24,b=8这相当于"32包含24在内所以除的整数部分并不影响结果，得到余数"
a=8,b=0,这就说明b（24）刚好可以被a（8）整除，而原来的32相当于24的一倍+8，所以显然是8的倍数

您的例子和解释很好地展示了辗转相除的过程！
核心思想是：两个整数的最大公约数等于其中较小的数和两数相除余数的最大公约数。
即 gcd(a, b) = gcd(b, a % b)。
通过不断用除数替换被除数，用余数替换除数，直到余数为0，此时的除数
（即最后一次的非零余数，或者说当b变为0时的a）就是最大公约数。
"""
# 第14题
"""
猜对了
"""
# 第15题
print(a:=sum(range(5, 101, 5)))

