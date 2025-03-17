from PIL import Image
import os


def resize_image(image_path, target_size=(150, 150)):
    """
    将图片调整为指定的大小。
    """
    with Image.open(image_path) as img:
        # 获取图片的尺寸
        width, height = img.size
        # 如果尺寸不是 150x150，调整大小
        if (width, height) != target_size:
            print(f"Resizing {image_path} from {width}x{height} to {target_size}")
            img_resized = img.resize(target_size)
            img_resized.save(image_path)  # 保存覆盖原文件
        else:
            print(f"Image {image_path} is already 150x150. No changes made.")


def resize_images_in_directory(directory, target_size=(150, 150)):
    """
    遍历指定目录，调整所有图片大小为 150x150（如果需要）。
    """
    for filename in os.listdir(directory):
        # 获取文件路径
        file_path = os.path.join(directory, filename)

        # 检查是否为文件而不是文件夹
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            resize_image(file_path, target_size)


# 指定要处理的文件夹路径
directory = r"D:\Desktop\code\ELAN-main\SR_datasets\WHU-RS19\test\LR"  # 替换为你自己的文件夹路径

# 调整文件夹中所有图片为 150x150
resize_images_in_directory(directory)
