# Learning ROS2

## Setup Env

### Option 1: Using VSCode

If you are using **VSCode** as your editor, follow these steps to set up the development environment inside a container:

1. Install the extension **"ms-vscode-remote.remote-containers"** in VSCode.
2. Press `Ctrl+Shift+P` to open the Command Palette.
3. Select **"Dev Containers: Rebuild and Reopen in Container"**.

Once completed, you are all set to start development inside the container.

### Option 2: Using Docker Compose

If you are not using VSCode, you can set up and run the development environment using Docker Compose:

1. Build and start the containers in detached mode:

```sh
docker-compose up -d
```

2. To access the container's shell, use:

```sh
docker exec -it ros2 bash
```

Once inside the container, you can begin your development work.

## Run turtlesim

```sh
ros2 run turtlesim turtlesim_node
```

TODO 也可以用 keyboard 試著操控 turtle (幫我補)


### Troubleshooting X Window Forwarding

```sh
# Disabling access control to the display
xhost +
# Enable access control to the display
xhost -
```

> macOS and Windows users might face additional issues with X Window forwarding.


## Create a Package

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
