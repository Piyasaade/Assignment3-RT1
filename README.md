# Piyasaade-Assignment3-RT1

# Description:
The main purpose of this project is to drive a robot in a specific map,and in a specific way that a user can choice.
the choices are the following:
1-the possibility to give a target position for the robot by choosing X and Y.
2-the possibility to drive the robot using the keyboard.
3-the possibility to drive the robot using the keyboard and avoiding obstacles.
If none of these choices have been chosen then the 4th choice will be to quit from the program.

# Command used to run the program:
from a linux shell we first launch the environment and the mapping nodes :
```bash
roslaunch final_assignment simulation_gmapping.launch 
roslaunch final_assignment move_base.launch
```
Then run the main code:
```bash
roslaunch P_code P_main.launch
```
# The structure:
**First** P_main.launch will be launched containing the P_userinterface srcipt which is responsible first to ask the user to choose one of the choices listed before.
Depending on the user's choice the functions used in the userinterface script will be run
**Second** if choice one is chosen, then the user has to enter the X and Y which will be responsible of the next destination/location of the robot.
client is used for this function and a timing is set in a way if the robot didn't reach the desired new position destinated from the user, then a message saying "Timed out achieving goal" will appear in the output shell , otherwise "Goal succeeded!" will be printed.
**Third** if choice 2 is chosen, then the function callen will launch "P_1.launch" containig the teleop_twist_keyboard node which is just responsible of the motion of the robot.
**Fourth** if choice 3 is chosen, then the fnction callen will launch "P_2.launch" containing the teleop_twist_keyboard node, obstacle_avoider.py script node and the cmd_vel topic. 
In that case, the cmd_vel topic is the connection between the node and the script, in a way that if the velocity and the direction given from the user passing through the topic will not lead to a collision then the robot can drive safely, otherwise, this values will be changed by detcting the obstacles using the laser scan topic.
**Fifth** if choice 4 is chosen, then the user chose to quit the program.
