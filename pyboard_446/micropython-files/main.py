import pyb
import led as led
import hid as hid


led.blink()
while True:
  hid.osc(100,50,3)
