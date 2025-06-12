# 第1题
"""
upper()将字符串变成PYTHON
替换将P变成J
所以是JYTHON
"""
from prompt_toolkit.key_binding.bindings.named_commands import capitalize_word

# 第2题
text = """
abc
       \"def
  hjk
"""
"""
\n和\t会解释为换行符和tap符
"""
# 第3题
"""
结果是Python
返回的是长度，也就是6
"""
# 第4题
text1 = "Programming"
print(text1[4])
print(text1[3:7])
print(text1[-3:])
# 第5题
mixed_case = "hELLo wORLd"
print(mixed_case.capitalize())
print(mixed_case.title())
print(mixed_case.lower())
# 第6题
"""
find可以指定从哪里开始找
find找不到会返回-1
而index找不到会报错
"""
# 第7题
"""
"Python3"调用isalpha()返回false，因为isalpha()判断仅仅字符
isalnum()返回true，因为isalnum()判断数字和字符
"""
# 第8题
item = "apple"
price = 1.256
print(f"The price of an{item} is ${price:.2f}.")
# 第9题
raw_input = "--- user_data ---"
print(raw_input.strip('-').strip())
# 第10题
sentence = "I like cats, cats are cute."
print(sentence.replace('cats', 'dogs',1))
# 第11题
data_string = "name:Alice;age:30;city:New York"
print(data_string.split(';'))
# 第12题
words = ['Python', 'is', 'fun']
print(' '.join(words))
# 第13题
unicode = "你好"
bytes_utf8 = unicode.encode('utf-8')
Decode =  bytes_utf8.decode('gbk')
print(Decode)
"""
很显然字不一样
"""
# 第14题
s = "loop"
for i in range(len(s)):
    print(s[i])
for str in s:
    print(str)
# 第15题
"""
字符串是不可变类型,每一次执行都会
1、创建一个新的字符串对象；
2、将原 result 和 short_string 的内容复制到新对象中；
3、更新 result 指向这个新对象。
很占内存，运行时间o2
可以使用列表收集所有字符串片段，最后统一拼接
"""