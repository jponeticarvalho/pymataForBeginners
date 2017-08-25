from pyfirmata import Arduino, util  # importa classe PyFirmata e time
import time                            
 
board = Arduino('/dev/ttyUSB0')  # em board criamos uma instancia usando a porta onde nosso arduino esta
  
def delay(second):
    time.sleep(second)  
 
def blink(second):
    # board --> porta digital --> pino 13 write -> 1 Ligado
    board.digital[13].write(1)  
    delay(second)
    # board --> porta digital --> pino 13 write -> 0 desligado
    board.digital[13].write(0)
    delay(second)

def blink2(second):
    """
    It lets you specify what pin you need by a string,
    composed of a or d (depending on wether you need
    an analog or digital pin), the pin number, and the mode
    (i for input, o for output, p for pwm).
    All seperated by :
    """

    pin13.write(1)
    delay(second)
    pin13.write(2)
    delay(second)

def leAnalog():
    arg = pinA.read()
    print arg


pin13 = board.get_pin('d:13:o')
pinA = board.get_pin('a:3:i')


x = 0
while x < 10:
    x = x + 1
    print x
    blink2(1)

