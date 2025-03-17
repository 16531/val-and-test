import os
import shutil
import random

# train_ratio代表分割后训练集占原数据集的比率
def split_data(image_folder, train_ratio=0.5):
    # 获取所有图片和标签文件的路径列表
    image_files = os.listdir(image_folder)
 #   label_files = os.listdir(label_folder)

    # 随机打乱文件列表
    random.shuffle(image_files)

    # 计算划分的训练集和验证集的边界索引
    split_index = int(len(image_files) * train_ratio)

    # 分割训练集和验证集
    train_images = image_files[:split_index]
    val_images = image_files[split_index:]

    # 创建训练集和验证集文件夹
    train_folder = 'train_data'
    val_folder = 'val_data'
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)

    # 将训练集的图片和标签移动到训练集文件夹
    for image_file in train_images:
        shutil.move(os.path.join(image_folder, image_file), os.path.join(train_folder, image_file))
        #corresponding_label = image_file.split('.')[0] + '.txt'
        #shutil.move(os.path.join( corresponding_label), os.path.join(train_folder, corresponding_label))

    # 将验证集的图片和标签移动到验证集文件夹
    for image_file in val_images:
        shutil.move(os.path.join(image_folder, image_file), os.path.join(val_folder, image_file))
        #corresponding_label = image_file.split('.')[0] + '.txt'
       # shutil.move(os.path.join( , os.path.join(val_folder, corresponding_label))

# 用法示例
image_folder_path = r'D:\Desktop\code\python-bianhao\valandtest'
# label_folder_path = r'D:\Desktop\code\xiaodan\SR_datasets\AID\train\LR'
split_data(image_folder_path, train_ratio=0.5)