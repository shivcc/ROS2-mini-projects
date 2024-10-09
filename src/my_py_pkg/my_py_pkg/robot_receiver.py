#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
class Receiver_robot(Node): 
    def __init__(self):
        super().__init__("robot_station_subscriber") 
        self.subscriber_= self.create_subscription(String,"robot_news", self.callback_Robot_news, 10)
        self.get_logger().info("Robot receiver is listening...")

    def callback_Robot_news(self, msg):
        self.get_logger().info(msg.data)


    
 
def main(args=None):
    rclpy.init(args=args)
    node = Receiver_robot() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()