import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped

class RobotTrajectory(Node):
    def __init__(self):
        super().__init__("robot_trajectory")

        self.tranjectory_sub_ = self.create_subscription(Odometry, "bumperbot_controller/odom", self.tranjectoryCallback, 10)
        self.path_pub_ = self.create_publisher(Path, "/bumperbot_controller/trajectory", 10)
        self.path_msg_ = Path()
        

    def tranjectoryCallback(self, msg):
        
        self.curve_ = PoseStamped()

        self.curve_.header = msg.header
        self.curve_.pose = msg.pose.pose
        
        self.path_msg_.header = msg.header 
        self.path_msg_.poses.append(self.curve_)
        self.path_pub_.publish(self.path_msg_)


def main():
    rclpy.init()
    robot_trajectory = RobotTrajectory()
    rclpy.spin(robot_trajectory)
    robot_trajectory.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()