# 第1题
"""
还有两个参数是打开文件的模式，比如说r是只如，w只写，a追加，r+读写等等，以及打开文件的编码比如UTF-8
作用：你可以按照需求调整打开文件的模式，如果要二进制就可以加个b，而编码则是适配不同的编译器
"""
from os.path import exists

# 第2题
"""
w的光标在文件开头，如果文件存在会覆盖
a的光标在文件末尾，如果文件存在会追加写入
"""
# 第3题
"""
可以确保文件在操作完成后（即使发生异常）自动关闭
"""
# 第4题
"""
read()：如果括号内没有传参就是全部读取，有传参就是读取多少个字符
readline()： 读取一行，包括末尾的换行符
readlines():  全读，返回一个字符串列表
"""
# 第5题
"""
file.write(string) 将string写入文件，返回写入的字符数
file.writelines(list_of_strings) 写入字符串列表，但是不会自动添加换行符
"""
# 第6题
"""
file.tell()方法的作用是输出查看当前文件指针位置
file.seek(0, 0)这条语句会将文件指针移动到哪里？ 文件开头
"""
# 第7题
"""
os.getcwd()函数返回当前操作目录
os.chdir(path)函数的作用是改变当前目录到path
"""
# 第8题
"""
os.listdir(path) 列出指定目录下的文件和子目录名，返回列表。
避免发生格式上的问题，使用当前系统的分隔符
"""
# 第9题
"""
os.mkdir(path) 创建一个目录
os.makedirs(path) 递归创建目录
父目录不存在会报错？我猜的
"""
# 第10题
"""
os.remove(path) 删除文件
os.rmdir(path) 删除目录，限制是只能删除空目录
用shutil的shutil.rmtree(path
"""
# 第11题
"""
os.path.exists(path) 判断路径是否存在
os.path.isfile(path) 判断是否是文件
os.path.isdir(path) 判读是否是目录
"""
# 第12题
import os
full_path = "/usr/local/bin/python"
print(os.path.basename(full_path)) # python
print(os.path.dirname(full_path)) # /usr/local/bin
# 第13题
"""
需要遍历目录树，可以产生一个含当前目录，目录下文件，字目录三元组
"""
# 第14题
words_to_create = "hello world \n My name is Maverick \n I'm 19 years old\n"
with open("data.txt", "w",encoding="UTF-8") as f:
    f.write(words_to_create)
try:
    with open( "data.txt", "r", encoding="UTF-8") as f:
        for i, line in enumerate(f):
            print(line.strip())
            i += 1
        print(f"There are {i} lines")
except FileNotFoundError:
        print("Error")
except IOError as e:
    print(f"An IO error occurred: {e}")

os.remove("data.txt") # 删除文件


#-----------------------------------------------------------------更简洁
# sum(1 for _ in open("data.txt", "r", encoding="UTF-8"))
# 这个方法利用了生成器表达式和 sum，内存效率高
try:
    with open("data.txt", "r", encoding="UTF-8") as f:
        line_count = sum(1 for _ in f)
    print(f"There are {line_count} lines")
except FileNotFoundError:
    print("Error: File not found.")


# 第15题
current_directory = os.getcwd()

if not os.path.exists("my_folder"):
    try:
        os.mkdir("my_folder")
    except FileExistsError: print("OHNO")

os.path.join(current_directory, "my_folder")

if not os.path.exists("notes.txt"): open("notes.txt", "w").close()
os.path.join( "my_folder", "notes.txt")
print(os.path.isfile("notes.txt"))
if os.path.exists("notes.txt"):
    os.remove("notes.txt")


# 补充思考：对于14题和15题我觉得我的内容有点长了，有没有更pythonic的方法，或者更简短一点的实现方法

#----------------------------------------------------------------------
import os
folder_name = "my_folder_concise"
file_name = "notes_concise.txt"
file_path = os.path.join(folder_name, file_name)

try:
    os.makedirs(folder_name, exist_ok=True) # 创建目录，如果存在则忽略
    with open(file_path, 'w') as f:         # 在指定路径下创建文件
        pass                                # 创建空文件
    print(f"File '{file_path}' created successfully.")
except OSError as e:
    print(f"Error: {e}")

# 清理 (可选)
# if os.path.exists(file_path): os.remove(file_path)
# if os.path.exists(folder_name) and not os.listdir(folder_name): os.rmdir(folder_name)

