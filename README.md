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
![immagine](https://github.com/Piyasaade/Piyasaade-Assignment3-RT1/blob/main/RT1-Assignment3.jpg)  

**First** P_main.launch will be launched containing the P_userinterface srcipt which is responsible first to ask the user to choose one of the choices listed before.
Depending on the user's choice the functions used in the userinterface script will be run

**Second** if choice one is chosen, then the user has to enter the X and Y which will be responsible of the next destination/location of the robot.
client is used for this function and a timing is set in a way if the robot didn't reach the desired new position destinated from the user, then a message saying "Timed out achieving goal" will appear in the output shell , otherwise "Goal succeeded!" will be printed.

**Third** if choice 2 is chosen, then the function callen will launch "P_1.launch" containig the teleop_twist_keyboard node which is just responsible of the motion of the robot.

**Fourth** if choice 3 is chosen, then the fnction callen will launch "P_2.launch" containing the teleop_twist_keyboard node, obstacle_avoider.py script node and the cmd_vel topic. 
In that case, the cmd_vel topic is the connection between the node and the script, in a way that if the velocity and the direction given from the user passing through the topic will not lead to a collision then the robot can drive safely, otherwise, this values will be changed by detcting the obstacles using the laser scan topic.

**Fifth** if choice 4 is chosen, then the user chose to quit the program.

# Possible Improvements:

Using Gazebo plugins with ROS,Gazebo plugins give your models greater functionality and can tie in ROS messages and service calls for sensor output and motor input.
A plugin is a chunk of code that is compiled as a shared library and inserted into the simulation. The plugin has direct access to all the functionality of Gazebo.

**Some of their functionalties:**
1-let developers control almost any aspect of Gazebo
2-are self-contained routines that are easily shared
3-can be inserted and removed from a running system
**YOU should ue it when :**
1-you want to programmatically alter a simulation
2-move models, respond to events, insert new models given a set of preconditions you want a fast interface to gazebo.
**plugin types:**
There are currently 6 types of plugins
1-World
2-Model
3-Sensor
4-System
5-Visual
6-GUI
**Plugins available in gazebo_plugins**
CAMERA: `provides ROS interface for simulating cameras such as wge100_camera by publishing the CameraInfo and Image ROS messages as described in sensor_msgs.
MULTICAMERA: ynchronizes multiple camera's shutters such that they publish their images together. Typically used for stereo cameras, uses a very similar interface as the plain Camera plugin.
GPU LASER: simulates laser range sensor by broadcasting LaserScan message as described in sensor_msgs.
PLANAR MOVE PLUGIN: model plugin that allows arbitrary objects (for instance cubes, spheres and cylinders) to be moved along a horizontal plane using a geometry_msgs/Twist message. The plugin works by imparting a linear velocity (XY) and an angular velocity (Z) to the object every cycle.

