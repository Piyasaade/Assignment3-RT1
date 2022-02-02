#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3

#initializing the angulare an linear velocities

init = Vector3(0, 0, 0)
repost = Twist( init, init)



def take_action(info):
	# receiving the information from cmd_vel topic and publishet back to the robot under specific conditions
    global repost
    pub = rospy.Publisher('cmd_vel',Twist, queue_size=10)
    regions = {
    'fright': min(min(info.ranges[144:287]), 10),
    'front':  min(min(info.ranges[288:431]), 10),
    'fleft':  min(min(info.ranges[432:575]), 10),
    }


    if regions['front'] < 0.5:
	# if the distance is less than 0.5 stop the robot from driving forward
        repost.linear.x = 0
        
    elif regions['fleft'] < 0.5 or regions['fright'] < 0.5:
	#if the distance in the left and right regions is less than 0.5 the robot stops its rotation
        repost.angular.z = 0

    pub.publish(repost)

def clbk_remap(info):
    # getting the information from this topic responsible of the angular an linear velocity coming from the robot
    global repost
    repost = info



def main():


    rospy.init_node('obstacle_avoidance')

    rospy.Subscriber('/remap_cmd_vel', Twist, clbk_remap)

    rospy.Subscriber('/scan', LaserScan, take_action)

    rospy.spin()


if __name__ == '__main__':
    main()
