from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

turtle_name = 'turtle1'


def generate_launch_description():
    return LaunchDescription([
        Node(package="turtlesim", executable="turtlesim_node", name=turtle_name),
        ExecuteProcess(cmd=[
            'ros2', 'service', 'call', f'/{turtle_name}/teleport_absolute', 'turtlesim/srv/TeleportAbsolute',
            '"{x: 1.0, y: 1.0, theta: 0.0}"'
            '&&'
            'ros2', 'service', 'call', '/clear', 'std_srvs/srv/Empty', '{}'
        ],
                       shell=True),
        Node(package="turtle_navigation", executable="obstacle_detector_node", name="obstacle_detector"),
        Node(package="turtle_navigation", executable="motion_controller_node", name="motion_controller"),
    ])
