This package comes with a docker container. All the codes are located at /home/ubuntu/data folder and this is a mounted volume to the host system. 
Steps:
    run the docker compose command
     $ sudo docker-compose up -d 
    navigate to http://0.0.0.0:6081/ and you will be able to connect to VNC viewer
    

===================================================================================

Gazebo virtual environment 
 All the assents are located in gazebo_asset folder
 cardbox box 500mmx500mmx500mm with aruco marker (100mmx100mm, no1)
 Warehouse model with container

Mobile manipulater
    run $ roslaunch mirabb_rev2_description gazebo.launch
    This will launch gazebo model of mobile manipulater
    run $ rosrun teleop_twist_keyboard teleop_twist_keyboard.py
    This will let you drive mobile base
    camera added

====================================================================================
To do
    Joints of the robot arms are fixed. So arm is not functional
    Laser range must be adjusted
    2 laser has to be combined and republish as single topic
    rosnav is not configured for autonomus navigation
   

====================================================================================

docker run -p 6080:80 --shm-size=512m tiryoh/ros-desktop-vnc:noetic
sudo docker-compose up -d --shm-size=512m
