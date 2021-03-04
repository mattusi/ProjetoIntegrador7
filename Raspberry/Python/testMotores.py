import time
from control_motores import *

MotorsSetup()

BaseSpeed(100)
print(100)
time.sleep(3)
print('turning')
Direction(50)
time.sleep(10)
MotorsStop()
print('Stop')