import time
import signal
import sys
from PyMata.pymata import PyMata

board = PyMata("/dev/ttyUSB0")

# Digital pins
GREEN_LED = 13

# Switch states
ON = 1
OFF = 0

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Set pin modes
board.set_pin_mode(GREEN_LED, board.OUTPUT, board.DIGITAL)

i=0
while i<10:
    board.digital_write(GREEN_LED, ON)
    time.sleep(1)
    board.digital_write(GREEN_LED, OFF)
    time.sleep(1)

# Do nothing loop - program exits when latch data event occurs for
# potentiometer or timer expires
time.sleep(15)
print('Timer expired')
board.close()