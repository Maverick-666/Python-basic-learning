## 核心概念

- **循环结构**: 控制程序中某条或某些指令重复执行的结构。
    
- **Python中的循环类型**:
    
    - for-in 循环: 适用于明确知道循环次数或需要遍历可迭代对象（如范围、列表、字符串等）的场景。
        
    - while 循环: 适用于循环次数不确定，依赖于某个条件来持续执行的场景。
        
- **循环体**: 被循环控制的、具有相同缩进的代码块。
    

## 一、for-in 循环

### 1. 基本用法与 range() 函数

for-in 循环通常与 range() 函数结合使用来控制重复次数。

```
# 循环变量 i 会依次取到 range() 生成的序列中的每个值
for i in range(5):  # i 会是 0, 1, 2, 3, 4
    print(f"Iteration {i}")
```


- **range() 函数**:
    
    - range(stop): 生成从 0 到 stop-1 的整数序列。
        
        - range(5) -> 0, 1, 2, 3, 4
            
    - range(start, stop): 生成从 start 到 stop-1 的整数序列。
        
        - range(1, 6) -> 1, 2, 3, 4, 5
            
    - range(start, stop, step): 生成从 start 到 stop-1，步长为 step 的整数序列。
        
        - range(1, 10, 2) -> 1, 3, 5, 7, 9 (奇数)
            
        - range(10, 0, -2) -> 10, 8, 6, 4, 2 (递减偶数)
            

### 2. 循环变量的惯例

如果循环体中不需要使用循环变量的值，通常将其命名为下划线 _。

```
for _ in range(3):
    print("Hello!") # 不需要知道当前是第几次循环
```



### 3. 应用：求和

```
# 1到100求和
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050

# 1到100偶数求和 (方法1: if判断)
total_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even += i
print(total_even) # 2550

# 1到100偶数求和 (方法2: range步长)
total_even_step = 0
for i in range(2, 101, 2):
    total_even_step += i
print(total_even_step) # 2550

# 1到100偶数求和 (方法3: sum()函数)
print(sum(range(2, 101, 2))) # 2550
```



## 二、while 循环

### 1. 基本用法

当 while 后的条件表达式为 True 时，重复执行循环体。

```
# 1到100求和
total_w = 0
i_w = 1
while i_w <= 100:
    total_w += i_w
    i_w += 1  # 关键：必须在循环体内更新条件变量，否则可能死循环
print(total_w) # 5050
```


### 2. while True 与 break

可以使用 while True 创建一个理论上的无限循环（死循环），然后在循环体内部通过 if 条件配合 break 关键字来终止循环。

```
# 1到100偶数求和
total_wtb = 0
i_wtb = 2
while True:
    total_wtb += i_wtb
    i_wtb += 2
    if i_wtb > 100:
        break  # 当 i_wtb 大于 100 时跳出循环
print(total_wtb) # 2550
```


## 三、循环控制关键字：break 和 continue

- **break**: 立即终止当前所在的**整个循环结构**的执行，程序跳转到循环结构之后的下一条语句。
    
- **continue**: 立即结束**本次循环**中 continue 之后的剩余语句，并直接开始下一轮循环的判断和执行。
    

```
# continue 示例：只累加偶数
total_c = 0
for i_c in range(1, 11): # 1 to 10
    if i_c % 2 != 0:  # 如果是奇数
        continue      # 跳过本次循环的 total_c += i_c
    total_c += i_c
print(total_c) # 2 + 4 + 6 + 8 + 10 = 30
```



## 四、嵌套循环

一个循环结构内部可以包含另一个或多个循环结构。

```
# 打印九九乘法表
for i in range(1, 10):        # 外层循环控制行
    for j in range(1, i + 1): # 内层循环控制列
        print(f'{j}×{i}={i * j}', end='\t') # 输出当前项，不换行，用制表符分隔
    print() # 内层循环结束后换行
```


## 五、循环结构应用实例

### 1. 判断素数 (质数)

素数是大于1且只能被1和自身整除的整数。检查因子到 

```
nn​
```

 即可。

```
num = int(input('请输入一个正整数: '))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break # 找到因子，不是素数，跳出循环
if is_prime: print(f'{num}是素数')
else: print(f'{num}不是素数')
```


### 2. 最大公约数 (GCD)

- **方法1 (暴力枚举)**: 从两个数中较小的一个开始递减，找到第一个能同时整除两数的数。
    
    ```
    x = int(input('x = '))
    y = int(input('y = '))
    smaller = min(x, y)
    gcd = 1
    for i in range(smaller, 0, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break
    print(f'GCD: {gcd}')
    ```

    
- **方法2 (欧几里得算法/辗转相除法)**: 效率更高。
    
    ```
    a = int(input('a = '))
    b = int(input('b = '))
    while b: # 当 b 不为 0 时
        a, b = b, a % b # a 变为原来的 b，b 变为 a 除以 b 的余数
    print(f'GCD: {a}') # 当 b 为 0 时，a 即为最大公约数
    ```


### 3. 猜数字游戏

计算机随机生成一个数，玩家猜测，程序给出提示。

```
import random

answer = random.randrange(1, 101) # 1到100的随机数
counter = 0
while True:
    counter += 1
    num = int(input('请输入你猜的数字 (1-100): '))
    if num < answer: print('大一点.')
    elif num > answer: print('小一点.')
    else:
        print('猜对了!')
        break
print(f'你一共猜了{counter}次.')
```



## 总结

- for-in 循环适用于已知循环次数或遍历序列。
    
- while 循环适用于未知循环次数，依赖条件判断。
    
- break 用于完全跳出循环，continue 用于跳过当前迭代的剩余部分进入下一次迭代。
    
- 嵌套循环可以处理更复杂的重复任务。
    
- 选择合适的循环结构和算法对程序效率至关重要。
    

---

这份精炼版的Markdown文件应该能帮助您更好地聚焦核心知识点。

接下来，我将针对这份精炼内容中的每个主要知识点为您出一道题。您准备好了吗？