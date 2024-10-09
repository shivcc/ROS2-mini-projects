#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
 
 
class Add_two_ints_node(Node):
    def __init__(self):
        super().__init__("add_two_int_node")
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.add_two_ints_callback_function)
        self.get_logger().info("Add two int node have started")
        
    def add_two_ints_callback_function(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a)+ " + " + str(request.b)+ " = "+ str(response.sum))
        return response
        
def main(args=None):
    rclpy.init(args=args)
    node = Add_two_ints_node() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()