import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import functools
import time

class CmdGen(Node):

    def __init__(self):
        super().__init__('cmd_gen')
        self.timer = self.create_timer(0.2, self.loop)
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.loop_count = 0
        self.get_logger().info("cmd_gen_node [del_jrs] has been started")

    def loop(self):
        cmd_msg = Twist()
    
        if self.loop_count < 5:
            cmd_msg.linear.y = 1.0  
            cmd_msg.angular.z = 0.0 
        elif self.loop_count < 15:
            cmd_msg.linear.y = 0.0
            cmd_msg.angular.z = 1.57
        elif self.loop_count < 20: 
            cmd_msg.linear.x = 1.3  
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 30:
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = -1.95  
        elif self.loop_count < 35: 
            cmd_msg.linear.y = 1.5  
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 45:  
            cmd_msg.linear.y = 0.0
            cmd_msg.angular.z = 1.95
        elif self.loop_count < 50:  
            cmd_msg.linear.x = 0.9  
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 60: 
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = -1.95
        elif self.loop_count < 65: 
            cmd_msg.linear.y = 1.2
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 75: 
            cmd_msg.linear.y = 0.0
            cmd_msg.angular.z = 1.95
        elif self.loop_count < 80: 
            cmd_msg.linear.x = 0.6
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 90: 
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = -1.95
        elif self.loop_count < 98: 
            cmd_msg.linear.y = 1.2
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 108: 
            cmd_msg.linear.x = 1.0
            cmd_msg.linear.y = 0.0
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 118: 
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = -1.98
        elif self.loop_count < 123: 
            cmd_msg.linear.y = 0.6
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 133: 
            cmd_msg.linear.y = 0.0
            cmd_msg.angular.z = 1.98
        elif self.loop_count < 138: 
            cmd_msg.linear.x = 1.25
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 148: 
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = -1.98
        elif self.loop_count < 153: 
            cmd_msg.linear.y = 0.9
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 163: 
            cmd_msg.linear.y = 0.0
            cmd_msg.angular.z = 1.98
        elif self.loop_count < 171: 
            cmd_msg.linear.x = 1.05
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 181: 
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = -1.98
        elif self.loop_count < 186: 
            cmd_msg.linear.y = 1.35
            cmd_msg.angular.z = 0.0
        elif self.loop_count < 191: 
            cmd_msg.linear.y = 0.0
            cmd_msg.linear.x = -0.9725
        elif self.loop_count < 196:
            cmd_msg.linear.x = 0.0
            cmd_msg.linear.y = 1.1
        elif self.loop_count < 206:
            cmd_msg.linear.y = 0.0
            cmd_msg.angular.z = 2.36
        self.cmd_pub.publish(cmd_msg)
        self.loop_count += 1
        if self.loop_count > 206:
            self.loop_count = 0


def main(args=None):
    rclpy.init(args=args)
    cmd_gen = CmdGen()
    rclpy.spin(cmd_gen)
    cmd_gen.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()