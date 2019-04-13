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
