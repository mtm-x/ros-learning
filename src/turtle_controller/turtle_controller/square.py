#! /usr/bin/env python3


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen, TeleportAbsolute

class MoveSquare(Node):
    def __init__(self):
        super().__init__("move_turtle")

        self.pen_off_  = self.create_client(SetPen, "/turtle1/set_pen")
        self.cmd_vel_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # self.pose_value_ = self.create_subscription(Pose, "/turtle1/pose", self.callback_pose, 10)
        self.teleport_ = self.create_client(TeleportAbsolute, "/turtle1/teleport_absolute")

    def callback_teleport(self,x, y):
        tele = TeleportAbsolute.Request()
        tele.x = x
        tele.y = y

        future_obj = self.teleport_.call_async(request=tele)
        future_obj.add_done_callback(self.call_back)
        
    def call_back(self, future):
        cmd = Twist()
        cmd.linear.x = 1.0
        # cmd.angular.z = 1.0
        self.callback_pen_off(0)
        self.cmd_vel_.publish(cmd)

    def callback_pen_off(self, off):

        while not self.pen_off_.wait_for_service(1.0):
            self.get_logger().info("Waiting..")

        pen = SetPen.Request()
        pen.off = off

        future_object = self.pen_off_.call_async(request=pen)

        future_object.add_done_callback(self.callback_pen_future)

    def callback_pen_future(self, future):
        self.get_logger().info("Turing off the pen")

    
def main () :
    rclpy.init()
    obj = MoveSquare()
    obj.callback_pen_off(1)
    obj.callback_teleport(1.0,9.0)
    rclpy.spin(obj)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

