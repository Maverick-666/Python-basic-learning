# day_XX_file_os_operations.py

import os
import shutil # For more advanced file operations like copying, moving, recursive deletion
import time

# -----------------------------------------------------------------------------
# 一、Python 文件操作 (File I/O)
# 核心函数：open()
# -----------------------------------------------------------------------------
print("--- 1. Python 文件操作 ---")

# --- 1.1 open() 方法 ---
# open(file, mode='r', encoding=None)
# mode: 'r'(read), 'w'(write), 'a'(append), 'x'(create),
#       'b'(binary), 't'(text - default), '+'(read/write)

# 创建一个示例文件
file_content_demo = "Hello, Python learners!\nWelcome to file operations.\nThis is the third line."
try:
    with open("sample.txt", "w", encoding="utf-8") as f_write_demo:
        f_write_demo.write(file_content_demo)
    print("Created 'sample.txt' for demonstration.")
except IOError as e:
    print(f"Error creating sample file: {e}")

# --- 1.2 文件读取 ---
print("\n--- 1.2 文件读取 ---")
try:
    # 1.2.1 read([size]): 读取指定字节数或全部
    print("--- Reading entire file with read() ---")
    with open("sample.txt", "r", encoding="utf-8") as f_read_all:
        content_all = f_read_all.read()
        print(content_all)

    print("\n--- Reading first 10 chars with read(10) ---")
    with open("sample.txt", "r", encoding="utf-8") as f_read_some:
        content_some = f_read_some.read(10)
        print(f"First 10 chars: '{content_some}'")
        print(f"Current position after read(10): {f_read_some.tell()}")

    # 1.2.2 readline([size]): 读取一行
    print("\n--- Reading line by line with readline() ---")
    with open("sample.txt", "r", encoding="utf-8") as f_readline_demo:
        line1 = f_readline_demo.readline()
        print(f"Line 1: {line1.strip()}") # strip() to remove trailing newline
        line2 = f_readline_demo.readline()
        print(f"Line 2: {line2.strip()}")

    # 1.2.3 readlines([sizeint]): 读取所有行并返回列表
    print("\n--- Reading all lines with readlines() ---")
    with open("sample.txt", "r", encoding="utf-8") as f_readlines_demo:
        lines_list = f_readlines_demo.readlines()
        print(f"List of lines: {lines_list}")
        for i, line_item in enumerate(lines_list):
            print(f"Line {i+1} from list: {line_item.strip()}")

    # 1.2.4 迭代文件对象 (推荐的逐行读取方式)
    print("\n--- Iterating through file object (recommended for line by line) ---")
    with open("sample.txt", "r", encoding="utf-8") as f_iterate_demo:
        for line_iter in f_iterate_demo:
            print(line_iter.strip())

except FileNotFoundError:
    print("Error: sample.txt not found. Please ensure it exists or was created.")
except IOError as e:
    print(f"An IO error occurred: {e}")


# --- 1.3 文件写入 ---
print("\n--- 1.3 文件写入 ---")
# 1.3.1 'w' 模式: 覆盖写入 (如果文件不存在则创建)
try:
    with open("output_w.txt", "w", encoding="utf-8") as fw:
        fw.write("This is the first line written with 'w' mode.\n")
        fw.write("This will overwrite existing content or create a new file.\n")
    print("Content written to 'output_w.txt' (overwrite mode).")

    # 1.3.2 'a' 模式: 追加写入 (如果文件不存在则创建)
    with open("output_a.txt", "a", encoding="utf-8") as fa:
        fa.write(f"Appending a new line at {time.ctime()}.\n")
    print("Content appended to 'output_a.txt'.")
    with open("output_a.txt", "a", encoding="utf-8") as fa: # Append again
        fa.write(f"Appending another line at {time.ctime()}.\n")
    print("Another line appended to 'output_a.txt'.")


    # 1.3.3 writelines(sequence): 写入字符串序列
    lines_to_write = ["Line A from writelines.\n", "Line B from writelines.\n"]
    with open("output_writelines.txt", "w", encoding="utf-8") as fwl:
        fwl.writelines(lines_to_write)
    print("Content written to 'output_writelines.txt' using writelines.")

except IOError as e:
    print(f"An IO error occurred during writing: {e}")

# --- 1.4 with 语句 (上下文管理器) ---
# 推荐使用 with open(...) as f:
# 它能确保文件在代码块执行完毕后自动关闭，即使发生异常。
# (上面的例子已经使用了 with)

# --- 1.5 文件指针操作 (seek, tell) ---
print("\n--- 1.5 文件指针操作 ---")
try:
    with open("sample.txt", "r+", encoding="utf-8") as f_seek_tell:
        print(f"Initial position: {f_seek_tell.tell()}") # 0
        first_char = f_seek_tell.read(1)
        print(f"Read first char: '{first_char}', New position: {f_seek_tell.tell()}") # 1

        f_seek_tell.seek(0) # 移动到文件开头 (offset 0, whence 0 by default)
        print(f"Position after seek(0): {f_seek_tell.tell()}") # 0
        first_word = f_seek_tell.read(5)
        print(f"Read first 5 chars again: '{first_word}'")

        f_seek_tell.seek(7, 0) # 移动到第7个字节 (offset 7, from start 0)
        print(f"Position after seek(7,0): {f_seek_tell.tell()}")
        f_seek_tell.write("REPLACED") # 在当前位置写入 (会覆盖)

    # 验证写入
    with open("sample.txt", "r", encoding="utf-8") as f_verify:
        print(f"\nContent of sample.txt after seek and write:\n{f_verify.read()}")

except IOError as e:
    print(f"An IO error occurred with seek/tell: {e}")

# --- 1.6 其他文件对象方法 ---
# flush(): 刷新缓冲区
# fileno(): 返回文件描述符
# isatty(): 是否连接到终端
# truncate([size]): 截断文件
# (这些方法使用场景相对特定，此处不详细演示)

# -----------------------------------------------------------------------------
# 二、OS 模块 (与操作系统交互，文件/目录操作)
# -----------------------------------------------------------------------------
print("\n\n--- 2. OS 模块 ---")

# --- 2.1 获取和改变当前工作目录 ---
current_dir_os = os.getcwd()
print(f"Current Working Directory: {current_dir_os}")
# os.chdir('path_to_change_to') # 改变目录 (小心执行，会改变脚本的相对路径基准)

# --- 2.2 列出目录内容 ---
print(f"\nListing current directory content:")
try:
    dir_content = os.listdir('.') # '.' 表示当前目录
    print(dir_content)
except OSError as e:
    print(f"Error listing directory: {e}")

# --- 2.3 创建和删除目录 ---
dir_to_create = "my_test_directory"
file_in_dir = os.path.join(dir_to_create, "test_file.txt") # os.path.join 跨平台路径拼接
dir_to_remove_recursive = "outer_dir/inner_dir"

print(f"\n--- Creating and Removing Directories ---")
# 2.3.1 mkdir(): 创建单个目录
if not os.path.exists(dir_to_create):
    try:
        os.mkdir(dir_to_create)
        print(f"Directory '{dir_to_create}' created.")
    except OSError as e:
        print(f"Error creating directory '{dir_to_create}': {e}")
else:
    print(f"Directory '{dir_to_create}' already exists.")

# 2.3.2 makedirs(): 递归创建目录 (包括中间目录)
if not os.path.exists(dir_to_remove_recursive):
    try:
        os.makedirs(dir_to_remove_recursive)
        print(f"Directory '{dir_to_remove_recursive}' created recursively.")
    except OSError as e:
        print(f"Error creating directory '{dir_to_remove_recursive}': {e}")
else:
    print(f"Directory '{dir_to_remove_recursive}' already exists.")


# 2.3.3 rmdir(): 删除空目录
if os.path.exists(dir_to_create):
    # 先确保目录为空，如果之前创建了文件，需要先删除文件
    if os.path.exists(file_in_dir): # 假设我们之前在这个目录里创建了文件
        try:
            os.remove(file_in_dir)
            print(f"File '{file_in_dir}' removed before rmdir.")
        except OSError as e:
            print(f"Error removing file '{file_in_dir}': {e}")
    try:
        os.rmdir(dir_to_create)
        print(f"Directory '{dir_to_create}' removed.")
    except OSError as e: # 例如目录不为空会报错
        print(f"Error removing directory '{dir_to_create}' with rmdir: {e}")

# 2.3.4 removedirs(): 递归删除空目录 (如果父目录也为空则一并删除)
# shutil.rmtree(): 强制递归删除目录及其所有内容 (更常用但需小心)
if os.path.exists(dir_to_remove_recursive):
    try:
        # removedirs 会尝试删除 inner_dir, 然后是 outer_dir (如果它们都为空)
        # os.removedirs(dir_to_remove_recursive)
        # 更常用的是 shutil.rmtree 来删除整个目录树，无论是否为空
        shutil.rmtree("outer_dir") # 删除 "outer_dir" 及其所有内容
        print(f"Directory tree 'outer_dir' removed using shutil.rmtree.")
    except OSError as e:
        print(f"Error removing directory '{dir_to_remove_recursive}' recursively: {e}")


# --- 2.4 删除文件 ---
file_to_delete_os = "temp_file_for_deletion.txt"
try:
    with open(file_to_delete_os, "w") as f_temp_del:
        f_temp_del.write("This file will be deleted.")
    print(f"\nFile '{file_to_delete_os}' created for deletion test.")
    os.remove(file_to_delete_os)
    print(f"File '{file_to_delete_os}' removed successfully.")
except IOError as e:
    print(f"Error creating/removing '{file_to_delete_os}': {e}")
except FileNotFoundError:
    print(f"Error: File '{file_to_delete_os}' not found for deletion (should not happen here).")


# --- 2.5 重命名文件或目录 ---
old_name_os = "old_filename.txt"
new_name_os = "new_filename.txt"
try:
    with open(old_name_os, "w") as f_old:
        f_old.write("Original content.")
    print(f"\nFile '{old_name_os}' created for rename test.")
    os.rename(old_name_os, new_name_os)
    print(f"File '{old_name_os}' renamed to '{new_name_os}'.")
    # 清理
    if os.path.exists(new_name_os): os.remove(new_name_os)
except IOError as e:
    print(f"Error creating/renaming file: {e}")
except FileNotFoundError:
    print(f"Error: File not found during rename (should not happen here).")

# --- 2.6 os.path 模块 (常用路径操作) ---
print("\n--- os.path module examples ---")
path_example_os = os.path.join(current_dir_os, "sample.txt") # 跨平台路径拼接
print(f"Constructed path: {path_example_os}")
print(f"Does path exist? {os.path.exists(path_example_os)}")
print(f"Is it a file? {os.path.isfile(path_example_os)}")
print(f"Is it a directory? {os.path.isdir(path_example_os)}")
print(f"Absolute path: {os.path.abspath('sample.txt')}")
print(f"Directory name: {os.path.dirname(path_example_os)}")
print(f"Base name (file name): {os.path.basename(path_example_os)}")
print(f"Split extension: {os.path.splitext(path_example_os)}") # ('path/to/sample', '.txt')
print(f"File size (bytes): {os.path.getsize(path_example_os) if os.path.exists(path_example_os) else 'N/A'}")

# --- 2.7 其他 os 方法 ---
# os.access(path, mode): 检查权限
# os.chmod(path, mode): 修改权限
# os.stat(path): 获取文件/目录状态信息
# os.getenv(key): 获取环境变量
# os.system(command): 执行系统命令 (通常 subprocess 模块更推荐)
# os.walk(top): 遍历目录树

# 示例：os.walk
print("\n--- os.walk example (listing files in current dir and subdirs) ---")
# 创建一些临时目录和文件用于walk演示
if not os.path.exists("walk_test_dir"): os.makedirs("walk_test_dir/sub_dir")
if not os.path.exists("walk_test_dir/file1.txt"): open("walk_test_dir/file1.txt", "w").close()
if not os.path.exists("walk_test_dir/sub_dir/file2.txt"): open("walk_test_dir/sub_dir/file2.txt", "w").close()

for dirpath, dirnames, filenames in os.walk("."): # 从当前目录开始
    # 为了避免遍历过多内容，我们只打印 "walk_test_dir" 相关的内容
    if "walk_test_dir" in dirpath or dirpath == ".": # 简化演示
        print(f"Directory Path: {dirpath}")
        print(f"  Sub-directories: {dirnames}")
        print(f"  Files: {filenames}")
        if dirpath == "." and "walk_test_dir" not in dirnames: # 确保只在walk_test_dir下深入
            break # 避免遍历整个项目目录，只演示一层

# 清理walk测试目录
if os.path.exists("walk_test_dir"):
    shutil.rmtree("walk_test_dir")
    print("\nCleaned up 'walk_test_dir'")


# 清理本脚本创建的其他文件
if os.path.exists("sample.txt"): os.remove("sample.txt")
if os.path.exists("output_w.txt"): os.remove("output_w.txt")
if os.path.exists("output_a.txt"): os.remove("output_a.txt")
if os.path.exists("output_writelines.txt"): os.remove("output_writelines.txt")
print("Cleaned up other generated files.")

print("\n--- End of File and OS Operations Demo ---")