#!/usr/bin/env python

import rospy
import roslib
import sys
import battery_low_protocol
import infRect
import rospy
import subprocess
import roslaunch

class Manager():

	def __init__(self):
		while not rospy.is_shutdown():
			text = input("What would you like to do? \n[1] rosrun battery_low_protocol \n[2] roslaunch frontier \n[3] rosrun infRect \n[4] rosrun pano_maker\n")
			if text == 1:
				print("running battery_low_protocol.py")
				subprocess.call(['gnome-terminal', '-x', '/home/beyondlimits/catkin_ws/src/infRect/src/scripts/battery_low_protocol.py'])
			if text == 2:
				print("launching frontiercomplete.launch")
				uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
				roslaunch.configure_logging(uuid)
				launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/beyondlimits/catkin_ws/src/infRect/launch/frontiercomplete.launch"])
				launch.start()
				#infRect.talker()
			if text == 3:
				print("running infRect.py")
				subprocess.call(['gnome-terminal', '-x', '/home/beyondlimits/catkin_ws/src/infRect/src/scripts/infRect.py'])
			if text == 4:
				print("running pano_maker.py")
				subprocess.call(['gnome-terminal', '-x', '/home/beyondlimits/catkin_ws/src/infRect/src/scripts/pano_maker.py'])


if __name__ == '__main__':
    try:
        Manager()
    except rospy.ROSInterruptException:
        pass
