#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
 
class series_gen(Node): # 
    def __init__(self):
        super().__init__("series_gen") 
        self.counter = 0 # initializing counter
        self.publisher_ = self.create_publisher(String,"series_2",10)
        self.timer_ = self.create_timer(1.0,self.timer_callback)
        self.get_logger().info("Series gen have started generating...")
        
    def timer_callback(self):
        self.counter += 2
        msg = String()
        msg.data = str(self.counter)
        self.publisher_.publish(msg)
        
 
def main(args=None):
    rclpy.init(args=args)
    node = series_gen() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()