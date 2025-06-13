from rclpy.node import Node
import rclpy
from example_interfaces.msg import Int64

class NumberPublisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.number_ = 2
        self.number_publisher_ = self.create_publisher(Int64,"number", 10)
        self.number_timer_ = self.create_timer( 1.0,self.publish_number)
    
    def publish_number(self):
        msg = Int64()
        msg.data=self.number_
        self.number_publisher_.publish(msg)

def main(agrs=None):
    rclpy.init(args=agrs)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()