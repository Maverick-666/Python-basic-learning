import random

# 第一种导入方式（导入模块math）
import math

# 使用方法：模块名.函数（函数）
print(math.log2(8))
print(math.log(2, 16))

# 第二种导入方式： from 模块名字 import *
from math import *

print(math.log2(8))
print(math.log10(100))

# 第三种导入方式（精确导入）： from 模块名字 import log2,1og10
from math import log2, log10

# 第四种：改成别称更简洁（也能解决命名冲突）
import multiprocessing as mp

# 第五种：
from math import log2 as lg2

print(lg2(8))


