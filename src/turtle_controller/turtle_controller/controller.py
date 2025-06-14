#! usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from my_robot_interfaces.srv import ActivateTurtle

class TurtleSim(Node):
    def __init__(self):
        super().__init__("turtle_controller")

        self.cmd_vel_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_value_ = self.create_subscription(Pose, "/turtle1/pose", self.callback_pose, 10)
        self.set_pen_ = self.create_client(SetPen, "/turtle1/set_pen")
        self.activate_ = self.create_service(ActivateTurtle, "activate_turtle", self.callback_activate_turtle)

    def callback_activate_turtle(self, request : ActivateTurtle.Request, response : ActivateTurtle.Response):
        self.activate_ = request.activate

        if request.activate :
            self.get_logger().info("TRUEEEEEEEEEEEEEEEEE")

        else :
            self.get_logger().info("FALSEEEEEEEEEEEEEE")


    def callback_pose(self, pose : Pose):
        cmd = Twist()
        if self.activate_:
            current_pose_ = pose.x
            if current_pose_ < 5.5:
                cmd.linear.x = 1.0
                cmd.angular.z = 1.0
                self.callback_set_pen(255,0,0)
            else:
                cmd.linear.x = 2.0
                cmd.angular.z = 2.0
                self.callback_set_pen(0,255,0)

            self.cmd_vel_.publish(cmd)

    def callback_set_pen(self, r, g, b):
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b

        future_obj = self.set_pen_.call_async(request=request)
        future_obj.add_done_callback(self.callback_future)

    def callback_future(self,future):
        self.get_logger().info("changed the colour")

def main():
    rclpy.init()
    obj = TurtleSim()
    rclpy.spin(obj)
    rclpy.shutdown()

if __name__ == "__main__":
    main()