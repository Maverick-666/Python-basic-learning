# 第一种
my_name = '张三'
my_age = 32
my_city = 'beijing'

print('我的名字是%s' % my_name)

print('我的名字是%s,我的年龄是%d' % (my_name, my_age))
print('我的名字是%s,我的年龄是%s,我所在的城市是%s' % (my_name, my_age, my_city))

# 特殊的格式化
money = 8923
num = 1.71

print('我的金额是：%5d' % money)
print('我的金额是：%d' % money)
# 不同点在于前者可以对齐

# 精确到小数点后一位:四舍五入
print('%.1f' % num)
print('%.2f' % num)

num02 = 22.345
print('%.2f' % num02)
'''
精确到小数点后两位应该是22.35，为什么？
因为计算机只认识和处理二进制二点数值，进行计算和转换
'''
# 精确的四舍五入
from decimal import Decimal

print(Decimal(str(num02)).quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))

# 第二种格式化
print(f'我的名字是{my_name},我的年龄是{my_age + 1},我所在的城市是{my_city}')
