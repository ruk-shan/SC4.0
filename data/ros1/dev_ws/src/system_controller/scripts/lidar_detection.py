#!/usr/bin/env python3

#detects the edge of the container

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):

    lidar_angle_range = (len(msg.ranges))

    
#   #If the distance to an obstacle in front of the robot is bigger than 1 meter, the robot will move forward
#   if msg.ranges[lidar_angle_range] > 1:
#       move.linear.x = 0.5
#       move.angular.z = 0.0

#   #If the distance to an obstacle in front of the robot is smaller than 1 meter, the robot will stop
#   if msg.ranges[360] < 1:
#       move.linear.x = 0.0
#       move.angular.z = 0.0

#   pub.publish(move)

rospy.init_node('container_detector')
sub = rospy.Subscriber('/scan_multi', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()