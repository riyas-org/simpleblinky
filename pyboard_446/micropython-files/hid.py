import pyb
import math
hid = pyb.USB_HID()
def osc(n, d, k):
  for i in range(n):
    hid.send((0, int(k * math.sin(i / 10)), 0, 0))
    pyb.delay(d)

