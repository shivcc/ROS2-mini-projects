#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
 
class modify_series(Node): # 
    def __init__(self):
        super().__init__("modify_series") 
        self.subscriber_= self.create_subscription(String,"series_2", self.subscriber_callback, 10)
        self.publisher_ = self.create_publisher(String,"series_4",10)
        self.get_logger().info("Series have started modifying...")
        
    def subscriber_callback(self, msg):
        #msg = String()
        #self.get_logger().info(msg.data) #for debug
        msg_int = int(msg.data)
        msg.data = str(msg_int*2)
        self.publisher_.publish(msg)
        
 
def main(args=None):
    rclpy.init(args=args)
    node = modify_series() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()