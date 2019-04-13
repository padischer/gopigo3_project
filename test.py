
import time
from easygopigo3 import EasyGoPiGo3

car = EasyGoPiGo3()

car.stop()
car.forward(50)
car.stop()
car.backward(50)
car.stop()