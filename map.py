#!/usr/bin/env python
import easygopigo3 as easy
import time
import sys


sensor_readings = None

gpg = easy.EasyGoPiGo3()


print('go on')
try:
    my_linefollower = gpg.init_line_follower()
    time.sleep(0.1)
except:
    print('Line Follower not responding')
    time.sleep(0.2)
    exit()


print("Still running")
print(my_linefollower.read_position())

#while True:
#    print(my_linefollower.read_position())
#    print(not  my_linefollower.read_position() == "white")

#    time.sleep(1)

#sys.exit(0)



# start
gpg.forward()
while not  my_linefollower.read_position() == "black":

    print(my_linefollower.read_position())

    if my_linefollower.read_position() == 'center':
        gpg.forward()
    if my_linefollower.read_position() == 'left':
        gpg.left()
        gpg.left()
        gpg.left()
    if my_linefollower.read_position() == 'right':
        gpg.right()
        gpg.right()
        gpg.right()


points = {
	"heinz": {
		"sven": ["forward", "forward"],
		"milo": ["right", "right"],
		"claudio": ["forward", "right", "left"],
		"start": ["forward", "right", "forward"],
		"chruch": ["left"],
		"cinema": ["forward", "left"],
		"lake": ["right", "forward"]
	},

	"milo": {
		"sven": ["forward", "left", "right"],
		"claudio": ["forward", "forward"],
		"heinz": ["left", "left"],
		"start": ["forward", "right"],
		"church": ["left", "forward"],
		"cinema": ["forward", "left", "forward"],
		"lake": ["right"]
	},

	"sven": {
		"milo": ["forward", "left", "right"],
		"claudio": ["left", "left"],
		"heinz": ["forward", "forward"],
		"start": ["left", "forward"],
		"church": ["forward", "right"],
		"cinema": ["right"],
		"lake": ["forward", "left", "forward"]
	},

	"claudio": {
		"sven": ["right", "right"],
		"milo": ["forward", "forward"],
		"heinz": ["forward", "right", "left"],
		"start": ["left"],
		"church": ["forward", "right", "forward"],
		"cinema": ["right", "forward"],
		"lake": ["forward", "left"]
	},

	"start": {
		"sven": ["forward", "right"],
		"milo": ["left", "forward"],
		"claudio": ["right"],
		"heinz": ["froward", "left", "forward"],
		"church": ["forward", "left", "right"],
		"cinema": ["forard", "forward"],
		"lake": ["left", "left"]
	},

	"church": {
		"sven": ["left", "forward"],
		"milo": ["forward", "right"],
		"claudio": ["forward", "left", "forward"],
		"heinz": ["right"],
		"start": ["forward", "left", "right"],
		"cinema": ["left", "left"],
		"lake": ["forward", "forward"]
	},

	"cinema": {
		"sven": ["left"],
		"milo": ["forward", "right", "forward"],
		"claudio": ["forward", "left"],
		"heinz": ["right", "forward"],
		"start": ["forward", "forward"],
		"church": ["right", "right"],
		"lake": ["forward", "right", "left"]
	},

	"lake": {
		"sven": ["forward", "right", "forward"],
		"milo": ["left"],
		"claudio": ["right", "forward"],
		"heinz": ["forward", "left"],
		"start": ["right", "right"],
		"church": ["forward", "forward"],
		"cinema": ["forward", "right", "left"]
	}
}

import sys 
from pprint import pprint 



waypoints = sys.argv
del waypoints[0]

previouswaypoint = None
for waypoint in waypoints:
	if previouswaypoint is not None:
		print("fahre von %s zu %s" % (previouswaypoint, waypoint))
		instructions = points[previouswaypoint][waypoint]
		for instruction in instructions:
			if instruction is "forward":
				print("car.forward()")
			if instruction is "left":
				print("car.spin_left(90)")
			if instruction is "right":
				print("car.spin_right(90)")


	previouswaypoint = waypoint















gpg.forward()
while not  my_linefollower.read_position() == "black":

    print(my_linefollower.read_position())

    if my_linefollower.read_position() == 'black':
        gpg.drive_cm(6)
        if my_linefollower.read_position() == 'center':
        	


    if my_linefollower.read_position() == 'left':
        gpg.left()
        gpg.left()
        gpg.left()
    if my_linefollower.read_position() == 'right':
        gpg.right()
        gpg.right()
        gpg.right()
