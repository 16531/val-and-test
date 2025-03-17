import os
import shutil


def move_and_rename_files(source_directory, target_directory):
    # 检查目标目录是否存在，如果不存在则创建
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # 用来保存文件的总数量（用于编号，从 0 开始）
    file_count = 0

    # 遍历目录及子目录中的所有文件
    for root, dirs, files in os.walk(source_directory):
        for filename in files:
            # 获取文件的完整路径
            old_file_path = os.path.join(root, filename)

            # 获取文件扩展名
            file_extension = os.path.splitext(filename)[1]

            # 生成四位数字编号（从0开始）
            new_name = f"{file_count:04d}{file_extension}"

            # 增加计数器
            file_count += 1

            # 构造新的文件路径（目标目录）
            new_file_path = os.path.join(target_directory, new_name)

            # 移动并重命名文件
            try:
                shutil.move(old_file_path, new_file_path)
                print(f"Moved and renamed: {filename} -> {new_name}")
            except PermissionError as e:
                print(f"PermissionError: Unable to move {filename}. {e}")
            except Exception as e:
                print(f"Error: Unable to move {filename}. {e}")


# 示例使用
source_directory = "D:\Desktop\code\WHU-RS19-4\X4"  # 替换为你的源文件夹路径
target_directory = "D:\Desktop\code\WHU-RS19-4\X4"  # 替换为你想将文件合并到的目标文件夹路径
move_and_rename_files(source_directory, target_directory)
# 示例使用
