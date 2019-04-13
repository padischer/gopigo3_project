
import time
from easygopigo3 import EasyGoPiGo3

car = EasyGoPiGo3()

car.forward()
time.sleep(5)
car.back()
time.sleep(5)

car.stop()