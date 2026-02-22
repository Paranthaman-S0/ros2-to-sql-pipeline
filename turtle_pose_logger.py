import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import csv
from datetime import datetime


class TurtlePoseLogger(Node):

    def __init__(self):
        super().__init__('turtle_pose_logger')

        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.listener_callback,
            10
        )

        self.file = open('turtle_pose.csv', 'w', newline='')
        self.writer = csv.writer(self.file)

        self.writer.writerow(
            ['time', 'x', 'y', 'theta', 'linear_velocity', 'angular_velocity']
        )

        self.get_logger().info('Logging turtle pose to turtle_pose.csv')


    def listener_callback(self, msg):
        now = datetime.now().isoformat()

        self.writer.writerow([
            now,
            msg.x,
            msg.y,
            msg.theta,
            msg.linear_velocity,
            msg.angular_velocity
        ])

        self.file.flush()


def main(args=None):
    rclpy.init(args=args)

    node = TurtlePoseLogger()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.file.close()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
