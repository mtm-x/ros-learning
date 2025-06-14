#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ResetCounter # custom interface for server/client 
#ros2 call <service_name> <interface_name> "<request_in_json>"
#ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r :0, g : 255, b : 0}"

class ServerClient(Node):
    def __init__(self):
        super().__init__("reset_counter_client")

        self.client_ = self.create_client(ResetCounter, "reset_counter")

    def call_reset_counter(self, value):

        while not self.client_.wait_for_service(1.0): # wait for the servers response ( checks every 1 seconds)
            self.get_logger().info("Waiting for server response")

        request = ResetCounter.Request() #creates an empty request object
        request.reset_value = value
        """
        Sends the Request: When you call call_async(), the ROS2 client immediately sends your request message over the network to the service server.
        Returns a Future Object: Crucially, call_async() does not wait for the response. Instead, it immediately returns a special object called a Future. 
        Think of this Future object as a "promise" or a "placeholder" for the eventual result of the service call. At the moment call_async returns, the Future is "not done" because the response hasn't arrived yet.
        """

        future = self.client_.call_async(request=request)
        """
        You can't directly access the result from a Future until it's "done." 
        Trying to access future.result() before it's done would block your program until it is.
        """
        future.add_done_callback(self.callback_reset_counter_response) #Hey, when you're finished, and you have the result (or an error), please call this specific function (self.callback_reset_counter_response)

    def callback_reset_counter_response(self, future):
        response = future.result()
        self.get_logger().info("success" + str(response.success))
        self.get_logger().info(str(response.message))

def main():
    rclpy.init()
    node = ServerClient()
    node.call_reset_counter(20)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
