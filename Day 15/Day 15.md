## 一、Python 文件操作 (File I/O)

### 1. 核心函数 open()

用于打开文件并返回文件对象。  
**基本语法**: file_object = open(file_path, mode='r', encoding='utf-8')

- file_path: 文件路径（相对或绝对）。
    
- mode: 打开模式 (见下表)。
    
- encoding: 文件编码，处理文本文件时强烈建议指定 (如 'utf-8')。
    

**常用文件打开模式 (mode)**:  

| 模式 | 描述 | 指针位置 | 文件不存在时 | 文件存在时 |
| :---: | :------: | :-------: | :---------: | :-----------: |
| r     | **只读**（默认） | 文件头 | 报错 | 读取 |
| w     | **只写** | 文件头 | 创建 | **覆盖** |
| a     | **追加** | 文件尾 | 创建 | 追加 |
| x     | **创建**，只用于写入 | 文件头 | 创建 | 报错 |
| rb    | 二进制只读 | 文件头 | 报错 | 读取 |
| wb    | 二进制只写 | 文件头 | 创建 | **覆盖** |
| ab    | 二进制追加 | 文件尾 | 创建 | 追加 |
| r+    | **读写** | 文件头 | 报错 | 读写 |
| w+    | **读写** | 文件头 | 创建 | **覆盖**读写 |
| a+    | **读写** | 文件尾 | 创建 | 追加读写 |

- b 可与 r, w, a, x, + 组合表示二进制模式 (如 rb, wb+)。
    
- t (文本模式) 是默认的，通常省略。
    

### 2. with 语句 (上下文管理器) - 推荐

使用 with open(...) as f: 可以确保文件在操作完成后（即使发生异常）自动关闭。

```python
try:
    with open('myfile.txt', 'w', encoding='utf-8') as f:
        f.write('Hello, world!\n')
        f.write('This is a test file.')
except IOError as e:
    print(f"文件操作错误: {e}")
```



### 3. 文件对象常用方法

- **读取**:
    
    - read([size]): 读取指定字节数（若size省略或为负，则读取全部内容）。
        
    - readline([size]): 读取一行（包括末尾的 \n）。
        
    - readlines([hint]): 读取所有行并返回一个字符串列表。
        
    - **迭代文件对象 (推荐)**: for line in file_object: (逐行读取)
        
- **写入**:
    
    - write(string): 将字符串写入文件。返回写入的字符数。
        
    - writelines(list_of_strings): 将字符串列表写入文件 (不会自动添加换行符)。
        
- **关闭文件**:
    
    - close(): 关闭文件，释放资源。**使用 with 语句时无需手动调用。**
        
- **文件指针**:
    
    - tell(): 返回文件指针的当前位置（字节数）。
        
    - seek(offset[, whence]): 移动文件指针。
        
        - whence=0 (默认): 从文件头开始计算 offset。
            
        - whence=1: 从当前位置开始计算 offset。
            
        - whence=2: 从文件尾开始计算 offset。
            
- **其他**:
    
    - flush(): 将内部缓冲区的数据立即写入磁盘。
        
    - fileno(): 返回文件的整数描述符。
        

```python
# 示例：读取
with open('myfile.txt', 'r', encoding='utf-8') as f:
    # content = f.read()
    for line in f:
        print(line.strip()) # strip() 移除首尾空白，包括换行符

# 示例：追加
with open('myfile.txt', 'a', encoding='utf-8') as f:
    f.write('\nAnother line appended.')
```



## 二、os 模块：与操作系统交互 (文件/目录)

需要先 import os。

### 1. 目录操作

- os.getcwd(): 获取当前工作目录路径。
    
- os.chdir(path): 改变当前工作目录到 path。
    
- os.listdir([path]): 列出指定目录（默认当前目录）下的文件和子目录名，返回列表。
    
- os.mkdir(path[, mode]): 创建单个目录。若已存在，抛出 FileExistsError。
    
- os.makedirs(path[, mode]): 递归创建目录（包括所有中间目录）。若已存在，抛出 FileExistsError (Python 3.2+ 可通过 exist_ok=True 避免报错)。
    
- os.rmdir(path): 删除**空**目录。若目录不空，抛出 OSError。
    
- os.removedirs(path): 递归删除空目录（如果父目录也变为空，则一并删除）。
    
    - **注意**: 对于非空目录的递归删除，通常使用 shutil.rmtree(path) (需要 import shutil)。
        

### 2. 文件操作

- os.remove(path) (或 os.unlink(path)): 删除文件。若文件不存在，抛出 FileNotFoundError。
    
- os.rename(src, dst): 重命名文件或目录，从 src 到 dst。
    
- os.stat(path): 获取文件或目录的元数据（如大小、修改时间等）。
    

### 3. os.path 子模块：路径操作 (跨平台)

os.path 模块提供了许多处理路径字符串的实用函数。

- os.path.join(path1[, path2[, ...]]): **智能地拼接路径**，使用适合当前操作系统的分隔符。
    
- os.path.exists(path): 判断路径是否存在 (文件或目录)。
    
- os.path.isfile(path): 判断路径是否为文件。
    
- os.path.isdir(path): 判断路径是否为目录。
    
- os.path.abspath(path): 返回路径的绝对路径。
    
- os.path.basename(path): 返回路径中的文件名部分。
    
- os.path.dirname(path): 返回路径中的目录部分。
    
- os.path.splitext(path): 分割路径为 (文件名主体, 扩展名) 的元组。
    
- os.path.getsize(path): 返回文件大小 (字节)。
    

```python
import os
import shutil # 导入 shutil 用于 rmtree

# 示例
current_path = os.getcwd()
print(f"当前目录: {current_path}")

new_dir = os.path.join(current_path, "test_dir")
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"目录 '{new_dir}' 已创建")

file_path = os.path.join(new_dir, "example.txt")
with open(file_path, 'w') as f:
    f.write("OS module test.")

print(f"'{file_path}' 是文件吗? {os.path.isfile(file_path)}")

# 清理 (示例)
# if os.path.exists(file_path): os.remove(file_path)
# if os.path.exists(new_dir): os.rmdir(new_dir) # 或 shutil.rmtree(new_dir) 如果可能不为空
```


### 4. 其他常用 os 功能

- os.walk(top): 遍历目录树，为 top 目录下的每个目录（包括top自身）生成一个三元组 (dirpath, dirnames, filenames)。
    
- os.access(path, mode): 检查路径的访问权限。
    
- os.getenv(key): 获取环境变量。
    
- os.system(command): 执行系统命令 (通常推荐使用更安全的 subprocess 模块)。
    

## 总结

- 文件操作是程序与外部数据持久化交互的基础。open() 函数和文件对象方法提供了读写文本和二进制文件的能力。**with 语句是管理文件资源的推荐方式**，确保文件正确关闭。
    
- os 模块及其子模块 os.path 提供了与操作系统底层交互的强大功能，用于管理文件系统中的文件和目录，是编写健壮、跨平台脚本的重要工具。