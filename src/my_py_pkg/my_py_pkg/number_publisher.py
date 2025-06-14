#!/usr/bin/env python3
#you can publish to a topic directly from the Terminal with ros2 topic pub -r <frequency> <topic_name> <interface> <message_in_json>
#how to change a node name at runtime—that is, by adding --ros-args -r __node:=<new_name>
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class PublishingNode(Node):
    def __init__(self):
        super().__init__("Publish_Node")
        self.number_to_publish_ = 69
        self.publish_ = self.create_publisher(Int64,"Numb",10)
        self.timer_ = self.create_timer(1.0, self.publisher)
        self.get_logger().info("Number publisher has been started.")
    
    def publisher(self):
        msg = Int64()
        msg.data = self.number_to_publish_
        self.publish_.publish(msg=msg)
        self.get_logger().info(f"Publishing {self.number_to_publish_}")

def main():
    rclpy.init()
    obj = PublishingNode()
    rclpy.spin(obj)
    rclpy.shutdown()

if __name__ == "__main__":
    main()