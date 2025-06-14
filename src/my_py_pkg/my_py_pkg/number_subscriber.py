#! /usr/bin/env python3

# ros2 topic echo <topic_name> direct subscription via cli
#I recommend naming callback methods for topics callback_<topic>
# changing the topic name in run time ros2 run my_py_pkg thisissub --ros-args -r Numb:=number

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from my_robot_interfaces.srv import ResetCounter


class NumberSubscriber(Node):
    def __init__(self):
        super().__init__("topic_sub")
        self.subscriber_ = self.create_subscription(Int64, "Numb", self.callback_Numb, 10)
        self.counter_ = 0
        self.is_active_ = True
        self.reset_counter_service_ = self.create_service(ResetCounter, "reset_counter", self.callback_reset_counter) #you can only have one service server but multiple clients.

    def callback_reset_counter(self, request : ResetCounter.Request, response : ResetCounter.Response):
        if request.reset_value < 0:
            response.success = False
            response.message = "NO negative"

        elif request.reset_value > self.counter_:
            response.success = False
            response.message = "Greater then counter itself"

        else:
            self.counter_ = request.reset_value
            response.success = True
            response.message = " Reseted the counter" 
            self.get_logger().info("Reset counter to " + str(self.counter_))
        
        return response

    def callback_Numb(self, msg: Int64):
        self.counter_ += msg.data
        self.get_logger().info("Printing the received Publishing topic in Numb : " + str(self.counter_))


def main():
    rclpy.init()
    obj = NumberSubscriber()
    rclpy.spin(obj)
    rclpy.shutdown()

if __name__ == "__main__":
    main()