#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class TurtleController(Node):

    def __init__(self):
        super().__init__("turtle_controller")

        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)


    def pose_callback(self, msg):
        x = float(msg.x)
        y = float(msg.y)

        msg = Twist()
        msg.linear.x = 5.0
        if x > 8 or x < 2 or y > 8 or y < 2:
            msg.angular.z = 3.0
        
        self.cmd_vel_pub_.publish(msg)

def main(args = None):
    rclpy.init()

    node = TurtleController()
    rclpy.spin(node)

    rclpy.shutdown()