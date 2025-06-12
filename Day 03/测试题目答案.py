# 第1题
"""
顺序结构：自上而下一条一条执行语句
分支结构：在进行到某个语句时进行判断，根据不同情况进入不同分支
分支结构解决了分类讨论问题
"""

# 第2题
"""
这个只是随便举的例子，格式上应该有区分，四个空格缩进
def weight(n):
    if n>=150:
        return True
    else:
        if n>=100:
            return True
        elif n>=60:
            return True
        else:
            return False   
"""
# 第3题
"""
条件判断表达式
真的情况执行，假不执行
"""
# 第4题
"""
不能，因为一个if-else结构只会进入一个分支
"""
# 第5题
"""
Young Adult
python自上而下查看哪个符合，然后进入该条语句，发现分支结束以后跳出if-else
"""
# 第6题
"""
x的取值范围是[10,20)
等价于x>=10 and x<20
"""
# 第7题
"""
场景：分支情况很多的时候，或者是需要更直观的表现情况,后续执行只需要一行
case_: 在结构中相当于else，也就是默认情况，必须放在末尾
"""
# 第8题
"""
match command:
    case "start" | "run" : print( "Executing command")
"""
# 第9题
"""
嵌套分支是一个分支语句中嵌套另一个分支语序
由于多层嵌套会使程序显得难以阅读和复杂，所以不如扁平
"""
# 第10题
num = int(input("请输入一个整数"))
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")

# 第11题
a = int(input("请输入数字1："))
b = int(input("请输入数字2："))
c = str(input("请输入一个符号"))
match c:
    case "+" : print(a+b)
    case "-" : print(a-b)
    case "*" : print(a*b)
    case "/" : print(a//b)
    case "%" : print(a%b)
    case _: print("无效运算符")

# 第 12题
m = int(input("请输入月份"))
match m:
    case 3|4|5: print("春季")
    case 6 | 7 |  8: print("夏季")
    case 9 | 10 | 11: print("秋季")
    case 1 | 2 | 12 : print("冬季")
    case _: print("错误，无效月份")
# 第 13题
"""
0,"",None
"""
# 第14题
"""
if 和 else 在同一个分支中保持同样的缩进
"""
# 第15题
print('The given sides cannot form a triangle.')