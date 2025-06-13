#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyFirstNode(Node):
    def __init__(self):
        super().__init__("Node_name") #Node Name
        print("HEll")

def main():
    rclpy.init() # Intialize ROS communication
    mynode = MyFirstNode() # create the object
    rclpy.spin(mynode)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

        

