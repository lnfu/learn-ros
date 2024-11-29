# Learning ROS2

```sh
# Disabling access control to the display
xhost +
# Enable access control to the display
xhost -
```

## Create a project

```sh
# @src
ros2 pkg create --build-type ament_cmake <project_name>
ros2 pkg create --build-type ament_python <project_name>
```

## Build

```sh
# @/
colcon build
source ./install/setup.bash
```
