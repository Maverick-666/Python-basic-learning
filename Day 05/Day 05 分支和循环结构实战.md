## 核心思想

本单元旨在通过实际编程案例，巩固和深化对分支结构 (if-elif-else) 和循环结构 (for, while) 的理解与应用。掌握这些基础结构是编写复杂逻辑程序的关键。**唯有通过大量练习，才能从理解语法到熟练应用。**

## 实践案例

### 1. 100以内的素数

**问题**: 输出2到99之间所有的素数。  
**思路**:

1. 遍历2到99的每个数 num。
    
2. 对于每个 num，假设它是素数 (is_prime = True)。
    
3. 再用一个内层循环，从2遍历到 int(num**0.5)（素数判断优化：检查因子只需到其平方根）。
    
4. 如果 num 能被内层循环的任何数整除，则 num 不是素数，设置 is_prime = False 并用 break 跳出内层循环。
    
5. 内层循环结束后，如果 is_prime 仍为 True，则打印 num。
    

```
for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ") # 输出: 2 3 5 7 ... 97
```


### 2. 斐波那契数列

**问题**: 输出斐波那契数列中的前20个数。  
**定义**: 

```
F0=0,F1=1F0​=0,F1​=1
```

 (或 

```
F1=1,F2=1F1​=1,F2​=1
```

), 

```
Fn=Fn−1+Fn−2Fn​=Fn−1​+Fn−2​
```

 for 

```
n≥2n≥2
```

.  
**思路**:

1. 初始化两个变量 a 和 b 作为序列的前两项（例如，a=0, b=1）。
    
2. 循环20次。
    
3. 在每次循环中，先利用 a 和 b 计算出下一项，然后更新 a 和 b 的值，使其向前滚动。Python的多元赋值 a, b = b, a + b 非常适合此场景。
    
4. 打印当前计算出的项。
    

```
a, b = 0, 1 # F(0)=0, F(1)=1
for _ in range(20):
    # 如果要打印 F(1), F(2)...F(20)
    a, b = b, a + b # a 变为 F(n), b 变为 F(n+1)
    print(a, end=" ") # 输出: 1 1 2 3 5 ...
```


### 3. 寻找水仙花数 (100-999)

**问题**: 找出100到999之间所有的水仙花数。  
**定义**: N位数的各位数字的N次方和等于该数本身 (三位数即为立方和)。例: 

```
153=13+53+33153=13+53+33
```

。  
**思路**:

1. 遍历100到999的每个数 num。
    
2. 拆分 num 的个位、十位、百位：
    
    - 个位: low = num % 10
        
    - 十位: mid = (num // 10) % 10
        
    - 百位: high = num // 100
        
3. 判断 num == low**3 + mid**3 + high**3 是否成立。
    
4. 如果成立，则打印 num。
    

```
for num in range(100, 1000):
    low = num % 10
    mid = (num // 10) % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num, end=" ") # 输出: 153 370 371 407
```



- **附：正整数反转技巧**:
    
    ```
    num = 12389
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + (num % 10)
        num //= 10
    # print(reversed_num) # 98321
    ```
    

### 4. 百钱百鸡问题

**问题**: 公鸡5元/只, 母鸡3元/只, 小鸡1元/3只。用100元买100只鸡，问公鸡(x)、母鸡(y)、小鸡(z)各多少？  
**约束**:

1. ```
    x+y+z=100x+y+z=100
    ```
    
     (数量)
    
2. ```
    5x+3y+z/3=1005x+3y+z/3=100
    ```
    
     (钱)
    
3. ```
    x,y,z≥0x,y,z≥0
    ```
    
     且 
    
    ```
    zz
    ```
    
     是3的倍数。
    

**思路 (穷举法/暴力搜索)**:

- **方法1 (三层嵌套)**: 分别对公鸡、母鸡、小鸡的数量在其可能范围内进行循环，然后判断是否同时满足上述两个约束条件。
    
    - 公鸡 x: range(0, 21) (最多20只)
        
    - 母鸡 y: range(0, 34) (最多33只)
        
    - 小鸡 z: range(0, 101, 3) (最多100只，且是3的倍数)
        
- **方法2 (两层嵌套优化)**: 确定公鸡 x 和母鸡 y 的数量后，小鸡数量 z 可以直接通过 z = 100 - x - y 计算得出。然后只需判断 z 是否为非负数、3的倍数，并且总价是否为100。
    

```
# 方法2 (优化版)
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z >= 0 and z % 3 == 0 and (5 * x + 3 * y + z // 3 == 100):
            print(f'公鸡: {x}, 母鸡: {y}, 小鸡: {z}')
```



### 5. CRAPS赌博游戏

**核心规则**:

1. **首次掷骰 (两颗)**:
    
    - 7或11点: 玩家胜。
        
    - 2, 3或12点: 庄家胜。
        
    - 其他点数: 成为目标点数 (Point)，游戏继续。
        
2. **后续掷骰 (若游戏继续)**:
    
    - 掷出7点: 庄家胜。
        
    - 掷出目标点数: 玩家胜。
        
    - 其他: 继续掷。
        

**代码结构思路**:

1. 外层 while 循环控制玩家总资金 money > 0。
    
2. 内层 while True (或条件) 循环处理下注有效性。
    
3. 模拟掷骰子：random.randrange(1, 7) + random.randrange(1, 7)。
    
4. if-elif-else 判断首次掷骰结果。
    
5. 若游戏继续，进入另一个内层 while True 循环处理后续掷骰，直到分出胜负 (使用 break 跳出当局循环)。
    
6. 根据胜负更新玩家资金。
    

```
# 伪代码/核心逻辑片段
import random
money = 1000
while money > 0:
    # ... 下注 (debt) ...
    first_point = random.randrange(1,7) + random.randrange(1,7)
    if first_point in (7, 11): money += debt # 玩家胜
    elif first_point in (2, 3, 12): money -= debt # 庄家胜
    else: # 游戏继续，first_point 为目标点
        while True:
            current_point = random.randrange(1,7) + random.randrange(1,7)
            if current_point == 7: money -= debt; break # 庄家胜
            elif current_point == first_point: money += debt; break # 玩家胜
# print("游戏结束")
```

## 总结

分支和循环是编程的基石。通过这些实战例子，我们可以看到如何将这些基础结构组合起来解决实际问题。关键在于分析问题、拆解步骤，并将这些步骤转化为代码逻辑。**持续练习是提升编程能力的不二法门。**