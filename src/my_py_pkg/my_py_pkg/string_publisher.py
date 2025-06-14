#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class StringPublisher(Node):
    def __init__(self):
        super().__init__("string_node")
        self.string_pub_ = self.create_publisher(String,"StringTopic",10)
        self.timer_ = self.create_timer(1.0, self.callback_string_node)

    def callback_string_node(self):

        self.string_ = String() # self.string_ = example_interfaces.msg.String(data='')
        self.string_.data = "Hi" # self.string_ = example_interfaces.msg.String(data='Hi')
        self.string_pub_.publish(msg=self.string_) 
        self.get_logger().info(f"Publishing the message : {self.string_.data}")

def main():
    rclpy.init()
    obj = StringPublisher()
    rclpy.spin(obj)
    rclpy.shutdown()

if __name__ == "__main__":
    main()