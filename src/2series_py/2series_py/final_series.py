#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
class final_series(Node): 
    def __init__(self):
        super().__init__("final_series") 
        self.subscriber_= self.create_subscription(String,"series_4", self.callback_subscriber, 10)
        self.get_logger().info("Robot receiver is listening...")

    def callback_subscriber(self, msg):
        self.get_logger().info(msg.data)


    
 
def main(args=None):
    rclpy.init(args=args)
    node = final_series() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()