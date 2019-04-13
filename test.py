
import time
from easygopigo3 import EasyGoPiGo3
from di_sensors import line_follower

car = EasyGoPiGo3()

car.stop()
car.drive_cm(150)
car.stop()
car.turn_degrees(270)