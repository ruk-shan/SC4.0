#!/bin/sh

apt-get update  # To get the latest package lists

apt-get install ros-noetic-teleop-twist-keyboard -y
apt-get install ros-noetic-ros-control ros-noetic-ros-controllers -y
apt-get install python3-catkin-tools -y

#etc.
