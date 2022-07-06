#!/usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import tf
import numpy
from std_msgs.msg import String
from gazebo_msgs.msg import ContactsState
import math

def callback(data):
    rospy.loginfo(data.states[0].total_wrench.force.z)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("A_contact_sensor_state", ContactsState, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()