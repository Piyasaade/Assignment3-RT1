#! /usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import *
from actionlib_msgs.msg import *
import os    

#print the option menu on terminal and wait for a numerical answer by the user
def choices():
    print("Dear user you should choose one of these choices ")
    print("1 : this choice will give you the possibility to give a target position for the robot by choosing X and Y ")
    print("2 : this choice will give you the possibility to drive the robot using the keyboard")
    print("3 : this choice will give you the possibility to drive the robot using the keyboard and avoiding obstacles")
    print("4 : this choice will give you the possibility to quit the program")
    print()        
    return input("enter your choice here please:  ")
    
def callback_case1(x,y):
    
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    #waiting for the connection with the server
    client.wait_for_server()
    #create the goal
    goal = MoveBaseGoal()
    #set the goal parameter
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.orientation.w = 1
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    #send the goal
    client.send_goal(goal)
    finished_within_time = client.wait_for_result(rospy.Duration(60.0))
    if not finished_within_time:
        client.cancel_goal()
        rospy.loginfo("Timed out achieving goal")
        return -1
    else:
        rospy.loginfo("Goal succeeded!")
        return 1 
       
    

def case1():
    print("case 1")
    x = float(input("insert x: "))
    y = float(input("insert y: "))
    callback_case1(x,y)
# launching teleop twist to control the robot
def case2():
    print("the user chose case 2")
    #launch a path using os
    os.system("roslaunch P_code P_1.launch")
# launching teleop and obstacle avoider script 
def case3():
    print("the user chose case 3")
    os.system("roslaunch P_code P_2.launch") 

 
if __name__=="__main__":
    #initialize the ros node
    rospy.init_node('P_userinterface_node')
    while(1):
        #the choice will be updated in the variable choice
        choice = choices()
        if (choice == '1'):
            case1()
        elif (choice == '2'):
            case2()  
        elif (choice == '3'):
            case3()
        elif (choice == '4'):
            break
        else:
            print("this choice is not available")
