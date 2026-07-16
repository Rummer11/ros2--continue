import rclpy  #ros python 接口库
from rclpy.node import Node  #ros2节点类
import time #引入时间类
def main(args=None):
    rclpy.init(args=args) #ros2 python接口初始化
    node=Node("my_node") #创建ros2节点对象并进行初始化函数名是节点名
    while rclpy.ok():
        node.get_logger().info("hello world") #通过node的方法找到它日志里面的对象通过它里面的方法打印helloworld
        time.sleep(0.5)#按照0.5秒进行休眠，控制循环时间：一秒钟打印两次，只有ctrl c才能终结循环
    node.destroy_node()#销毁节点对象
    rclpy.shutdown()#关闭ros2python接口
