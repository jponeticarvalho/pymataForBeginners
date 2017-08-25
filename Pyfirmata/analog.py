from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')

def leAnalog():
    arg = pin.read()
    print arg

pin = board.get_pin('a:3:i')

it = util.Iterator(board)
it.start()

while(1):
    op = input('digite um valor')
    if op == 1:
        leAnalog()