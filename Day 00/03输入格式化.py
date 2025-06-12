# input() 会把接收到的任意用户输入的数据当作字符串处理
name = input('请输入你的名字:')
print(name)
print(type(name))

# 输入类型转换
age = input('请输入你的年龄:')
print(type(age))
age = int(age)
print(type(age))

info = '''你好
世界
'''

print(info)

