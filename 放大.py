import cv2
import numpy as np


def save_magnify(path, a, b):  # a:矩形框左上角坐标  ; b:矩形框右下角坐标
    imagee = cv2.imread(path)
    lw = 2
    # 截出放大的部分
    img_magnify = imagee[a[1] - lw:b[1] + lw, a[0] - lw:b[0] + lw, :]

    # 计算缩放比例
    new_W = imagee.shape[1] - 2 * lw
    ratio = float(new_W) / img_magnify.shape[1]

    # 根据缩放比例计算缩放后的尺寸
    new_height = int(img_magnify.shape[0] * ratio)
    new_size = (new_W, new_height)
    # 进行缩放
    resized_image = cv2.resize(img_magnify, new_size)

    # 添加边框
    border_size = lw
    border_color = (0, 0, 255)  # 红色
    resized_image = cv2.copyMakeBorder(resized_image, border_size, border_size, border_size, border_size,
                                       cv2.BORDER_CONSTANT, value=border_color)

    # 画矩形框
    cv2.rectangle(imagee, a, b, (0, 0, 255), lw)

    # 拼接
    patch = np.vstack((imagee, resized_image))
    cv2.imshow(path.split('\\')[-1], patch)
    cv2.waitKey(0)
    # cv2.imwrite("E:\png_jpg"+  '/' + path.split('\\')[-1],patch)


# 全局变量
drawing = False  # 是否正在绘制矩形框
start_x, start_y = -1, -1  # 矩形框左上角坐标
end_x, end_y = -1, -1  # 矩形框右下角坐标


def draw_rectangle(event, x, y, flags, param):
    global drawing, start_x, start_y, end_x, end_y

    if event == cv2.EVENT_LBUTTONDOWN:  # 左键击下
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:  # 左键弹起
        drawing = False
        end_x, end_y = x, y

    if drawing:
        # 绘制矩形框
        image_copy = image.copy()
        cv2.rectangle(image_copy, (start_x, start_y), (x, y), (0, 0, 255), 2)
        cv2.imshow("Image", image_copy)

    if not drawing and start_x != -1 and start_y != -1:
        # 显示矩形框的左上角和右下角坐标
        print(f"矩形框左上角坐标：({start_x}, {start_y})")
        print(f"矩形框右下角坐标：({end_x}, {end_y})")
        for i in range(1):
            save_magnify(image_path, a=(start_x, start_y), b=(end_x, end_y))
            save_magnify(image_path_2, a=(start_x, start_y), b=(end_x, end_y))
            break
        start_x = -1


if __name__ == '__main__':
    # 输入图像路径
    image_path = r'D:\Desktop\code\论文图片\802.jpg'
    image_path_1 = r'D:\Desktop\code\论文图片\802l.jpg'
    image_path_2 = r'D:\Desktop\code\论文图片\carn.jpg'
    image_path_3 = r'D:\Desktop\code\论文图片\esr.jpg'
    image_path_4 = r'D:\Desktop\code\论文图片\lgc.jpg'
    image_path_5 = r'D:\Desktop\code\论文图片\pan.jpg'
    image_path_6 = r'D:\Desktop\code\论文图片\vsdr.jpg'
    # 读取图像
    global imagee
    image = cv2.imread(image_path)

    # 创建窗口并显示图像
    cv2.namedWindow("Image")
    cv2.imshow("Image", image)

    # 设置鼠标回调函数
    cv2.setMouseCallback("Image", draw_rectangle)

    # 循环等待按键事件
    while True:

        key = cv2.waitKey(1) & 0xFF

        # 按下 'q' 键 或者 退出窗口时  退出程序
        if key == ord('w') or cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()
