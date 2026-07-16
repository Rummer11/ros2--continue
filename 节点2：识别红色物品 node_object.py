#!/usr/bin/env python3
import cv2
import numpy as np
import rclpy
from rclpy.node import Node

# 红色的HSV阈值（可调）
lower_red = np.array([0, 90, 128])
upper_red = np.array([180, 255, 255])

def object_detect(image):
    # 1. BGR -> HSV
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 2. 二值化：提取红色区域
    mask_red = cv2.inRange(hsv_img, lower_red, upper_red)

    # 3. 找轮廓
    contours, hierarchy = cv2.findContours(mask_red, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        # 4. 过滤小面积噪声（轮廓点数 < 150 忽略）
        if cnt.shape[0] < 150:
            continue

        # 5. 获取外接矩形
        x, y, w, h = cv2.boundingRect(cnt)

        # 6. 绘制轮廓（绿色，线宽2）
        cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)

        # 7. 绘制中心点（红色圆点，半径5）
        center_x = x + w // 2
        center_y = y + h // 2
        cv2.circle(image, (center_x, center_y), 5, (0, 0, 255), -1)

        # 8. 绘制外接矩形（蓝色）
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 显示结果
    cv2.imshow("object", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = Node("node_object")
    node.get_logger().info("ROS2节点示例测试程序")

    # 请把路径换成你电脑上实际的图片路径
    image_path = '/home/saber/picture/apple.jpg'
    image = cv2.imread(image_path)

    if image is None:
        node.get_logger().error("图片加载失败，请检查路径！")
    else:
        object_detect(image)

    rclpy.spin(node)  # 保持节点运行（也可以去掉，因为只处理一张图）
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
