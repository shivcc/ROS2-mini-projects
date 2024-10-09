#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class mynode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("Hello Ros2!!!"+ str(self.counter))
        self.create_timer(0.5, self.timer_callback)
       

    def timer_callback(self):
        self.counter += 1
        self.get_logger().info("hello " + str(self.counter))

def main(args=None):
    rclpy.init(args=args)
    node = mynode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()
