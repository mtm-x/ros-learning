#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyFirstNode(Node):
    def __init__(self):
        super().__init__("Node_name") #Node Name
        self.get_logger().error("ERROR")
        self.counter_ = 0
        self.timer_ = self.create_timer(0.5,self.print)

    def print(self):
        self.get_logger().info("HUH "+ str(self.counter_)) # logger always expects string
        self.counter_ += 1

def main():
    rclpy.init() # Intialize ROS communication
    mynode = MyFirstNode() # create the object
    rclpy.spin(mynode) # Making the node spin means that we block the execution here, the program stays alive, and thus the node stays alive
    rclpy.shutdown() # After the node is killed, shut down

if __name__ == "__main__":
    main()

        

