#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial
 
 
class Add_two_int_node(Node): 
    def __init__(self):
        super().__init__("add_two_int_client") 
        self.call_server_add_two_int(9,36)
        
    def call_server_add_two_int(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        #logger while waiting for server
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server add_two_int_server")
        
        #define the variables    
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
    
        #Call the server and store the result in future variable
        future = client.call_async(request)
        # We can't spin until future complete coz node already spinning
        # make a new callback that runs when future done
        future.add_done_callback(partial(self.callback_call_future_found, a=a, b=b))
        
        
    def callback_call_future_found(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a)+ " + " + str(b)+ " = "+ str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))
    
    
        
 
 
def main(args=None):
    rclpy.init(args=args)
    node = Add_two_int_node() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()