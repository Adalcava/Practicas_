import pyfirmata
import time
import inspect
import random

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
        
board=pyfirmata.Arduino('COM6')

it = pyfirmata.util.Iterator(board)
it.start()

pin11 = board.get_pin('d:11:s') # s para servo
angle = 0
angles = [18, 54, 90, 126, 162]


pin11.write(angle)
time.sleep(1)
pin11.write(180)
print(len(angles))
time.sleep(1)

def elegir_jugador(self):
    global angles
    if len(self)==0:
        angles = [18, 54, 90, 126, 162]
    else:
        angle=random.choice(self)
        pin11.write(angle)
        self.remove(angle)
        
    
while True:
    print(angles)
    elegir_jugador(angles)
    time.sleep(1)
    