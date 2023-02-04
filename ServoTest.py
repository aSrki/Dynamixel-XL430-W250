from XL430 import *
import time



parallel_rotate(7, 12, "s", "s", 0, 0)
time.sleep(2)
parallel_rotate(7, 12, "m", "m", 500, 700)
time.sleep(2)
parallel_rotate(7, 12, "m", "m", 0, 0)
