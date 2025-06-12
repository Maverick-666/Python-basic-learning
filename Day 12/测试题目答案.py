# 第1题
"""
可读性提高
节约开发时间，避免冗长代码
便于管理，包括其他地方复用
"""
# 第2题
"""
choices和sample函数的区别在于choices是可放回抽取，后者是不放回
对于数据安全来说，越多种组合意味着更安全，所以可放回数据比不放回数据量大，安全
"""
# 第3题
"""
code_len前的*意味着必须用关键字传入参数
调用的时候要用code_len = 一个数字
"""
# 第4题
"""
 int和-> bool是什么
 int是传入的参数的类型
 bool是return的类型
 他们对实际执行没影响，目的是让程序员更方便理解函数的使用，包括调用的时候需要注意到的传入传出参数
"""
# 第5题
"""
for循环寻找到根号n停止搜索，让原来O(n2)的时间复杂度变成O(n)
因为大于根号n的部分，加入能整除n，那么得到的商也是小于根号n的部分，而这是已经搜索过的了
"""
# 第6题
"""
体现了编程中函数的使用者可以不关心其内部实现细节，只需了解它的功能和接口就能根据工具得到结果
同时也有模块化和复用
"""
# 第7题
"""
我不太懂这个，于是查了资料
ddof参数的全称是Delta Degrees of Freedom，翻译为“自由度调整”。它主要用于控制标准差和方差的计算方式。具体来说，ddof参数的取值会影响标准差的计算公式：

ddof=0：计算总体标准差
ddof=1：计算样本标准差

ddof参数的主要作用是调整分母中的自由度。
对于总体标准差，分母是数据的总个数 ( n )；而对于样本标准差，分母是 ( n-1 )。
这种调整是为了在样本较小的情况下，得到一个无偏的估计。
"""
# 第8题
"""
奇数的话直接n/2，得到中间那个数
偶数的话则是求出中间两个数的平均值
"""
# 第9题
"""
choose_balls专门负责选择每轮抽到的球
display_balls专门负责展示抽到的球
两个函数各司其职，分工明确，如果出现问题只需要在相关的函数处找到问题
"""
# 第10题
def get_file_extension(filename: str) -> str:
    """
    输出文件格式，没有就输出""
    :param filename: 文件全名
    :return: 文件的格式，没有就""
    """
    return filename[filename.rfind('.')+1:].lower() if filename.find('.') != -1 else "\"\""
print(get_file_extension("image.JPG"))
print(get_file_extension("report"))
print(get_file_extension("backup.tar.gz"))
# 第11题
def convert_temperature(temp, from_scale, to_scale):
    """
    摄氏度和华氏度相互转换
    :param temp: 传入的温度（float)
    :param from_scale: 温度转换开始
    :param to_scale: 温度转换结束
    :return: 转换结束的温度
    """
    return "{:.2f}".format(temp * 9/5+32) if from_scale == 'C' and to_scale == 'F' else "{:.2f}".format((temp - 32)*5/9)
"""
为了训练一句话解决问题的能力，我省略了温标无效的情况，或者如果一句话就能写出来，请你教我
"""
print(convert_temperature(100.0,'F','C'))
print(convert_temperature(100.0,'C','F'))


def convert_temperature_robust(temp, from_scale, to_scale):
    if from_scale == 'C' and to_scale == 'F':
        return temp * 9/5 + 32
    elif from_scale == 'F' and to_scale == 'C':
        return (temp - 32) * 5/9
    elif from_scale == to_scale:
        return temp # 同温标无需转换
    else:
        # 处理无效温标，可以返回None，或引发ValueError
        print(f"错误：无效的温标转换 '{from_scale}' -> '{to_scale}'")
        return None
        # 或者 raise ValueError(f"无效的温标转换: {from_scale} -> {to_scale}")

# 第12题
"""
作用是让阅读者包括程序员更好理解，或者一眼看出来函数的功能，传入值和输出值
我上面定义的函数都有写这些，你应该知道我会查看了吧哈哈哈哈哈
"""
# 第13题
"""
设置默认值首先可以防止调用的时候忘记使用
同时也可以作为一个提醒，给调用提供参考
"""
# 第14题
"""
import可以导入python的库，其中包含丰富的函数
放在开头是因为很直观，而且模块在程序启动时一次性加载，避免重复加载 
"""
# 第15题
"""
这个原则很好的将一个细节的功能封装起来，调用的时候只需要知道他的功能和使用方法就能轻松调用
而且如果出问题了，也只需要focus on一个小块的函数部分，节省了很多debug的时间
"""