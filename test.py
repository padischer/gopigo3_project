
import time
from easygopigo3 import EasyGoPiGo3

car = EasyGoPiGo3()

car.stop()
car.drive_cm(150)
car.stop()
car.turn_degrees(270)