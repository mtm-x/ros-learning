#! usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleSim(Node):
    def __init__(self):
        super().__init__("turtle_controller")

        self.cmd_vel_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_value_ = self.create_subscription(Pose, "/turtle1/pose", self.callback_pose, 10)


    def callback_pose(self, pose : Pose):
        cmd = Twist()
        current_pose_ = pose.x
        if current_pose_ < 5.5:
            cmd.linear.x = 1.0
            cmd.angular.z = 1.0

        else:
            cmd.linear.x = 2.0
            cmd.angular.z = 2.0

        self.cmd_vel_.publish(cmd)

def main():
    rclpy.init()
    obj = TurtleSim()
    rclpy.spin(obj)
    rclpy.shutdown()

if __name__ == "__main__":
    main()