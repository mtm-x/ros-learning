#! /bin/usr/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class StringSubscriber(Node):
    def __init__(self):
        super().__init__("SubNode")
        self.string_sub_ = self.create_subscription(String,"StringTopic",self.callback_StringTopic,10)

    def callback_StringTopic(self, msg : String):
        self.get_logger().info(msg.data) 

def main ():
    rclpy.init()
    obj  = StringSubscriber()
    rclpy.spin(obj)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
