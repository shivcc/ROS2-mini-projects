#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from functools import partial
from my_robot_interfaces.msg import TurtleArray
from my_robot_interfaces.msg import Turtle
import random
 
 
class TurtSwnKll(Node): 
    def __init__(self):
        super().__init__("turtle_spwn_rm") 
        self.turtle_count = 1
        self.AliveTurts = []
        self.AliveTurtsClass = TurtleArray()
        self.spawn_timer = self.create_timer(1, self.spawn_timer_callback)
        
        self.alive_turtle_publisher = self.create_publisher(TurtleArray, "turtles_alive", 10)
        self.alive_turtle_subscriber = self.create_subscription(TurtleArray,"turtles_alive", self.update_alive, 10 )
 
    def spawn_timer_callback(self):
        self.turtle_count= self.turtle_count + 1
        turtle_name = "turtle" + str(self.turtle_count)
        x = float(random.randrange(0, 11))
        y = float(random.randrange(0, 11))
        theta = float(random.randrange(0, 3))
        self.call_server_spawn(x=x, y=y, theta=theta)
        
        turt = Turtle()
        turt.x = x
        turt.y = y
        turt.theta = theta
        turt.name = turtle_name
        
        self.AliveTurts.append(turt)
        self.AliveTurtsClass.turtles = self.AliveTurts
        self.alive_turtle_publisher.publish(self.AliveTurtsClass)
        
    def update_alive(self, msg):
        self.AliveTurtsClass = msg
        self.AliveTurts = self.AliveTurtsClass.turtles
        
    
    
    
    
    def call_server_spawn(self, x, y, theta):
        client = self.create_client(Spawn, "spawn")
        #logger while waiting for server
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server spawn server")
        
        #define the variables    
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
    
        #Call the server and store the result in future variable
        future = client.call_async(request)
        # We can't spin until future complete coz node already spinning
        # make a new callback that runs when future done
        future.add_done_callback(partial(self.callback_call_future_found, a=x, b=y))
        
        
    def callback_call_future_found(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info("turtle at (" + str(a)+ " , " + str(b)+ ") spawned with name:  "+ str(response.name))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))
    
        
        
def main(args=None):
    rclpy.init(args=args)
    node = TurtSwnKll() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()