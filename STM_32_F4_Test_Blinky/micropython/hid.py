import pyb
import math

hid = pyb.USB_HID()
led = pyb.Pin('LED', pyb.Pin.OUT_PP)  # 4 is the blue LED

def osc(n, d):
  for i in range(n):
    hid.send((0, int(20 * math.sin(i / 10)), 0, 0))
    pyb.delay(d)

# toggle LED state every second using on() and off() methods
while True:
  led.on()
  osc(100, 50)
  #pyb.delay(1000)
  led.off()
  pyb.delay(1000)
