import time
from PyMata.pymata import PyMata

board = PyMata("/dev/ttyUSB0")

board.i2c_config(0, board.ANALOG, 4, 5)

board.i2c_read(0x48, 0, 2, board.I2C_READ)

time.sleep(3)

data = board.i2c_get_read_data(0x48)