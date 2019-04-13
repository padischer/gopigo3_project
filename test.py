
import time
from easygopigo3 import EasyGoPiGo3

car = EasyGoPiGo3()

car.forward()
time.sleep(5)

car.stop()