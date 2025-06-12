# 第1题
"""
python的列表是存储元素的单元[]用中括号表示
无序（但可排序），可变，元素类型可样，而且可以同时存在（但不推荐）
"""
# 第2题
lst = [1,2,3]
lst2 = list(range(1,4))
# 第3题
a = []
b = ['x', 'y']
c = [1,2]
"""
我怀疑可能有打印错误，故补充了一个情况，以防万一
a + b = ['x', 'y']
b + c = ['x', 'y',1 ,2]
a * 2 = []
c * 2 = [1,2,1,2]
"""
# 第4题
my_list = ['P', 'y', 't', 'h', 'o', 'n']
print(my_list[3])
print(my_list[1:4])
print(my_list[::-1])
# 第5题
colors = ['red', 'green', 'blue']
for i in range(len(colors)):
    print(colors[i])
for color in colors:
    print(color)
"""
显然第二种更好
"""
# 第6题
"""
append是末尾追加
insert可以指定位置添加
"""
# 第7题
"""
remove()方法括号里面是删除的元素
pop()方法括号里面是删除的元素的索引，而且pop()方法返回删除的值
会报错，"x" is not in list
"""
# 第8题
"""
sort()是立刻排序，对原来的列表排序
而sorted()是新建一个排序的列表
"""
# 第9题
"""
题目中并没有给出data列表
我自己建一个data = [10,20,30,20,40]
data.index(20)结果是1
data.count(20)结果是2
data.index(50)会报错
"""
# 第10题
print([r**2 for r in range(0,9,2)])
# 第11题
words = ['apple', 'banana', 'kiwi', 'orange', 'grape']
print([word for word in words if len(word)>5])
# 第12题
"""
题目没有显示出来，我自己写
"""
matrix = [[1,2],3,[4,5,6]]
print(matrix[2][0])
# 第13题
print([[0 for _ in range(2) ] for _ in range(3)])
# 第14题
"""
因为点数和索引正好相差1，点数6对应索引5
"""
# 第15题
"""
random.sample(red_balls, 6)直接抽取6个，保证不会有重复
random.choice()放回，会重复
"""