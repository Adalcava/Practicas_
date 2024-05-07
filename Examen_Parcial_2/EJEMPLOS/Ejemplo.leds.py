import pyfirmata
import inspect
import time

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
    
board = pyfirmata.Arduino('/dev/cu.usbmodem14201')

while True:
    board.digital[13].write(1)
    time.sleep(0.5)
    board.digital[13].write(0)
    time.sleep(0.5)