import rclpy

import numpy as np

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import TeleportRelative


class MotionController(Node):

    def __init__(self) -> None:
        super().__init__('motion_controller')
        self.start = False
        self.dest = np.array([10.0, 10.0], dtype=np.float32)
        self.delta_time = 0.05
        self.vel = 1.0

        self.attraction_coef = 10.0

        self.tr_cli = self.create_client(TeleportRelative, 'turtle1/teleport_relative')
        while not self.tr_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('/turtle1/teleport_relative service not available, waiting again...')

        self.pose_subscription = self.create_subscription(Pose, '/turtle1/pose', self.get_location, 10)

        self.repulsion = np.zeros(2, dtype=np.float32)
        self.repulsion_subscription = self.create_subscription(Twist, '/turtle1/repulsion', self.get_repulsion, 10)

        self.timer = self.create_timer(self.delta_time, self.move_toward_dest)

    def get_repulsion(self, msg: Twist):
        self.repulsion = np.array([msg.linear.x, msg.linear.y], dtype=np.float32)

    def get_location(self, pose_msg: Pose):
        self.location = np.array([pose_msg.x, pose_msg.y], dtype=np.float32)
        self.theta = pose_msg.theta
        self.start = True

    def move_toward_dest(self):
        if not self.start:
            return

        diff = self.dest - self.location
        distance = np.linalg.norm(diff)
        if distance <= 0.5:  # TODO reach target
            self.get_logger().info('The turtle reach the destination.')
            self.timer.cancel()
            return

        attraction = self.attraction_coef * diff  # TODO 是否要 normalization?
        # TODO attraction 移動到別的 method

        force = attraction - self.repulsion

        angle = float(np.arctan2(force[1], force[0])) - self.theta

        req = TeleportRelative.Request()
        req.linear = self.vel * self.delta_time
        req.angular = angle
        self.tr_cli.call_async(req)


def main(args=None):
    rclpy.init(args=args)

    motion_controller = MotionController()

    rclpy.spin(motion_controller)

    motion_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
