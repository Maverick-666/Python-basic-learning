## 核心思想

本单元通过一系列实际编程案例，展示如何将相对独立且可能重复使用的功能封装成函数。这样做可以提高代码的模块化、可读性、可维护性和复用性。函数的参数（包括类型注解）和返回值（包括类型注解）使得函数接口更清晰。

## 实践案例

### 1. 随机验证码生成

**目标**: 创建一个函数，能生成指定长度的、由数字和大小写英文字母组成的随机验证码。  
**关键库/函数**:

- random.choices(population, k): 从 population 中进行 **有放回** 的随机抽样，抽取 k 个元素。返回一个列表。
    
- string.digits: 包含 '0123456789' 的字符串。
    
- string.ascii_letters: 包含所有大小写英文字母的字符串。
    
- ''.join(iterable): 将可迭代对象中的字符串元素连接成一个单一字符串。
    

```python
import random
import string

ALL_CHARS = string.digits + string.ascii_letters # 候选字符集

def generate_code(*, code_len: int = 4) -> str: # 命名关键字参数，带默认值和类型注解
    """生成指定长度的随机验证码。"""
    return ''.join(random.choices(ALL_CHARS, k=code_len))

# 使用示例
print(generate_code())          # 默认长度4
print(generate_code(code_len=6)) # 指定长度6
```



### 2. 判断素数 (质数)

**目标**: 创建一个函数，判断一个大于1的正整数是否为素数。  
**定义**: 素数是只能被1和自身整除的大于1的正整数。  
**优化思路**: 检查因子时，只需检查到该数的平方根即可。如果 

```
NN​
```

 之前没有因子，则 

```
NN​
```

 之后也不会有。

```python
def is_prime(num: int) -> bool:
    """判断一个正整数是否为素数。"""
    if num <= 1:
        return False # 素数定义大于1
    for i in range(2, int(num ** 0.5) + 1): # 检查到 sqrt(num)
        if num % i == 0:
            return False # 找到因子，不是素数
    return True # 未找到因子，是素数
```



### 3. 最大公约数 (GCD) 和最小公倍数 (LCM)

**目标**: 分别创建函数计算两个正整数的最大公约数和最小公倍数。  
**GCD思路 (欧几里得算法/辗转相除法)**: gcd(a, b) = gcd(b, a % b)，当 b 为0时，a 即为GCD。  
**LCM公式**: lcm(x, y) = (|x * y|) / gcd(x, y)。

```python
def gcd(x: int, y: int) -> int:
    """求最大公约数 (欧几里得算法)。"""
    while y: # 当 y 不为 0
        x, y = y, x % y
    return abs(x) # 返回正数

def lcm(x: int, y: int) -> int:
    """求最小公倍数。"""
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // gcd(x, y) # 使用整数除法
```


- **函数间调用**: lcm 函数内部调用了 gcd 函数，体现了函数的复用。
    

### 4. 数据描述性统计

**目标**: 创建一系列函数计算样本数据的基本描述性统计信息。

- **均值 (Mean)**: 
    
    ```python
    xˉ=∑xinxˉ=n∑xi​​
    ```
    
- **中位数 (Median)**: 排序后中间的数（或中间两数的均值）。
    
- **极差 (Range/PTP)**: 最大值 - 最小值。
    
- **样本方差 (Sample Variance)**: 
    
    ```
    s2=∑(xi−xˉ)2n−1s2=n−1∑(xi​−xˉ)2​
    ```
    
     (ddof=1)
    
- **样本标准差 (Sample Standard Deviation)**: 
    
    ```
    s=s2s=s2​
    ```
    
- **变异系数 (Coefficient of Variation)**: 
    
    ```
    CV=sxˉCV=xˉs​
    ```
    

````python
def mean(data: list) -> float:
    return sum(data) / len(data) if data else 0.0

def median(data: list) -> float:
    if not data: return 0.0
    s_data, n = sorted(data), len(data)
    return float(s_data[n//2]) if n % 2 != 0 else (s_data[n//2 - 1] + s_data[n//2]) / 2.0

def ptp(data: list) -> float: # Peak to Peak
    return float(max(data) - min(data)) if data else 0.0

def var(data: list, ddof: int = 1) -> float: # ddof (Delta Degrees of Freedom)
    if len(data) <= ddof: return 0.0
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - ddof)

def std(data: list, ddof: int = 1) -> float:
    return var(data, ddof) ** 0.5

def cv(data: list, ddof: int = 1) -> float:
    m = mean(data)
    return std(data, ddof) / m if m != 0 else float('inf')

def describe(data: list):
    print(f'均值: {mean(data):.2f}, 中位数: {median(data):.2f}, ...') # 示例
*   **ddof**: 自由度参数，用于区分样本统计量和总体统计量。
````


### 5. 双色球随机选号 (函数重构)
**目标**: 将之前双色球选号的逻辑封装成函数，提高代码的模块化和可读性。
*   `choose()`: 生成一组随机号码。
*   `display(balls)`: 格式化输出一组号码。

```python
RED_BALLS_POOL = list(range(1, 34))
BLUE_BALLS_POOL = list(range(1, 17))

def choose_balls() -> list:
    selected_reds = sorted(random.sample(RED_BALLS_POOL, 6))
    blue_ball = random.choice(BLUE_BALLS_POOL)
    selected_reds.append(blue_ball)
    return selected_reds

def display_balls(balls: list):
    red_str = " ".join(f"{ball:0>2d}" for ball in balls[:-1])
    blue_str = f"{balls[-1]:0>2d}"
    print(f"红球: {red_str} 蓝球: [{blue_str}]") # 简化输出

# 主程序逻辑
# num_sets = int(input('生成几注号码: '))
# for _ in range(num_sets):
#     display_balls(choose_balls())
````


- **好处**: choose_balls() 和 display_balls() 的内部实现可以独立修改和测试，主程序逻辑更清晰。调用者只需关心函数的输入和输出。
    

## 总结

- **函数封装**: 将特定功能组织成函数是良好编程实践的核心。
    
- **参数与返回值**: 清晰定义函数的输入（参数，可带类型注解）和输出（返回值，可带类型注解）能增强代码可读性和可维护性。
    
- **模块化与复用**: 函数使得代码更易于管理、测试和在不同地方复用。
    
- **抽象**: 函数的使用者可以不关心其内部实现细节，只需了解其功能和接口。
    
- Python标准库和第三方库提供了大量预先封装好的函数，极大地提高了开发效率。