FROM osrf/ros:humble-desktop

ENV UID=1000
ENV GID=1000
ENV USER=efliao

SHELL ["/usr/bin/bash", "-c"]

WORKDIR /ros2_ws

RUN apt-get update \
    && apt-get install -y \
    build-essential \
    vim \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# formatter
RUN /bin/python3 -m pip install -U yapf

# RUN  source /opt/ros/${ROS_DISTRO}/setup.bash

# add user/group, empty password, allow sudo
RUN groupadd -g ${GID} ${USER}
RUN useradd --uid ${UID} --gid ${GID} --groups root,sudo,adm,users --create-home --password "" --shell /bin/bash ${USER}
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /home/${USER}/.bashrc
