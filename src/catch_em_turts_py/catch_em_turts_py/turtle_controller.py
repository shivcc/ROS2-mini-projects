#!/usr/bin/env python3
import rclpy
import math

from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from geometry_msgs.msg import Twist
from my_robot_interfaces.msg import Turtle, TurtleArray
 
class TurtleControlNode(Node): 
    def __init__(self):
        super().__init__("turtle_control_node") 
        self.target = [5,5]
        self.current_pose = None
        self.AliveTurtsClass = TurtleArray()
        self.AliveTurts = []
        
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)
        self.control_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        
        self.alive_turts_subscriber = self.create_subscription(TurtleArray, "turtles_alive", self.alive_turts_callback, 10)
        self.alive_turtle_publisher = self.create_publisher(TurtleArray, "turtles_alive", 10)
        
        self.control_loop_ = self.create_timer(0.01, self.timer_callback)
        
    def pose_callback(self, msg):
        #self.get_logger().info("got pose")
        self.current_pose = msg
    
    def alive_turts_callback(self, msg):
        self.AliveTurtsClass = msg
        self.AliveTurts = self.AliveTurtsClass.turtles
        
        #Target gets updated
         
        nearest_turt = self.search_target(self.AliveTurts)
        
        self.target[0] = nearest_turt.x
        self.target[1] = nearest_turt.y
        
        
        #Kill turtle if reached target
        self.kill_turtle(nearest_turt, self.AliveTurts)
        
        
        #self.get_logger().info(str(self.AliveTurtsClass.turtles))   #debug
        
        
        
    def kill_turtle(self, turtle, AliveTurts):
        if self.current_pose == None:
            return
        
        
        if self.target[0] - 0.5 <= self.current_pose.x <= self.target[0] + 0.5 and self.target[1] - 0.5 <= self.current_pose.y <= self.target[1]+ 0.5:
            # Check if the turtle name exists in the AliveTurts list before removing 
            if turtle in AliveTurts: 
                AliveTurts.remove(turtle) 
                self.AliveTurtsClass.turtles = AliveTurts
                self.alive_turtle_publisher.publish(self.AliveTurtsClass)
                
                client = self.create_client(Kill, "kill")
                request = Kill.Request()
                request.name = turtle.name
                client.call_async(request)
                self.get_logger().info("Killed turtle: " + turtle.name)
                
                return
                
            else: 
                self.get_logger().warn(f"Turtle {turtle.name} not found in AliveTurts list")
            
            
            
            
            
            
        
    
    
    
    def search_target(self, turtles):
        if self.current_pose == None:
            return 0, 0
        
        
        turtle = Turtle()
        
        turtle_dist_list = []
        
        for turtle in turtles:
            Dist_x = turtle.x - self.current_pose.x
            Dist_y = turtle.y - self.current_pose.y
            Dist_to_target = math.sqrt((Dist_x * Dist_x) + (Dist_y * Dist_y))
            turtle_dist_list.append(Dist_to_target)
            
        
        nearest_turt = turtles[turtle_dist_list.index(min(turtle_dist_list))]
        
        return nearest_turt
        

    
    def timer_callback (self):
        if self.current_pose == None:
            return
        
        Dist_x = self.target[0] - self.current_pose.x
        Dist_y = self.target[1] - self.current_pose.y
        Dist_to_target = math.sqrt((Dist_x * Dist_x) + (Dist_y * Dist_y))
        Angle_diff = math.atan2(Dist_y,Dist_x) - self.current_pose.theta
        
        msg = Twist()
        
        if (Dist_to_target > 0.5):
            if Angle_diff > math.pi:
                Angle_diff -= 2*math.pi
            elif Angle_diff < -math.pi:
                Angle_diff += 2*math.pi
        
            msg.linear.x = 3 * Dist_to_target
            msg.angular.z = 8 * Angle_diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
    
        self.control_publisher_.publish(msg)   
         
        
        
        
        
 
 
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()