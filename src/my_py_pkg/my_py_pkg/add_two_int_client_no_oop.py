#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
 

def main(args=None):
    rclpy.init(args=args)
    
    #define node and client and service name
    node = Node("add_two_int_no_oop")
    client = node.create_client(AddTwoInts, "add_two_ints")
    
    #logger while waiting for server
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for server add_two_int_server")
        
    #define the variables    
    request = AddTwoInts.Request()
    request.a = 5
    request.b = 9
    
    #Call the server and store the result in future variable
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    
    #Possibility for exeption hence try exept structure
    #getr responce from future and print 
    try:
        response = future.result()
        node.get_logger().info(str(request.a)+ " + " + str(request.b)+ " = "+ str(response.sum))
    except Exception as e:
        node.get_logger().error("Service call failed %r" % (e,))
    
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()