#!/usr/bin/env python
import easygopigo3 as easy
import time
import sys
import logging
from driveby import mapguide
from pprint import pprint 
from driveby import car




logging.basicConfig(filename='driveby.log',level=logging.DEBUG)

sensor_readings = None

waypoints = sys.argv
del waypoints[0]


gpg = easy.EasyGoPiGo3()
mapguide = mapguide.mapguide()
car = car.car()
gpg.set_speed(200)

previouswaypoint = None

for waypoint in waypoints:
    if previouswaypoint is not None:
        logging.info("fahre von %s zu %s" % (previouswaypoint, waypoint))
        instructions = mapguide.guide(previouswaypoint, waypoint)
        logging.info(instructions)
        car.drive(instructions)
    previouswaypoint = waypoint

