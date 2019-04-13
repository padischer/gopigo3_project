
import time
from easygopigo3 import EasyGoPiGo3

car = EasyGoPiGo3()

car.stop()
car.drive_cm(50)
car.stop()
car.turn_degrees(90)