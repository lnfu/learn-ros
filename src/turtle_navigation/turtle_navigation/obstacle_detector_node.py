import rclpy

import numpy as np

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn


class ObstacleDetector(Node):

    def __init__(self) -> None:
        super().__init__('obstacle_detector')
        self.start = False
        self.obstacles = np.array([[3.0, 2.9], [5.0, 9.0], [6.5, 7.0]], dtype=np.float32)  # TODO multiple

        spawn_cli = self.create_client(Spawn, '/spawn')
        while not spawn_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('/spawn service not available, waiting again...')
        for id, obstacle in enumerate(self.obstacles):
            spawn_req = Spawn.Request()
            spawn_req.x = float(obstacle[0])
            spawn_req.y = float(obstacle[1])
            spawn_req.name = f'obstacle{id+1}'
            spawn_cli.call_async(spawn_req)

        self.repulsion_coef = 100.0
        self.repulsion_threshold = 1.5

        self.pose_subscription = self.create_subscription(Pose, 'turtle1/pose', self.get_location, 10)
        self.repulsion_publisher = self.create_publisher(Twist, '/turtle1/repulsion', 10)

    def get_location(self, pose_msg: Pose):
        location = np.array([pose_msg.x, pose_msg.y], dtype=np.float32)

        repulsion = np.zeros(2, dtype=np.float32)
        for obstacle in self.obstacles:
            diff = obstacle - location
            distance = np.linalg.norm(diff)
            if distance <= self.repulsion_threshold:
                if distance == 0.0:  # TODO
                    distance = 0.001
                repulsion += self.repulsion_coef * diff / (distance**3)

        repulsion_msg = Twist()
        repulsion_msg.linear.x = float(repulsion[0])
        repulsion_msg.linear.y = float(repulsion[1])

        self.repulsion_publisher.publish(repulsion_msg)


def main(args=None):
    rclpy.init(args=args)

    obstacle_detector = ObstacleDetector()

    rclpy.spin(obstacle_detector)

    obstacle_detector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
