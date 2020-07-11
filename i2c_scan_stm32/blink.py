#test beacon led on python codec board

import pyb



led = pyb.Pin('PE13', pyb.Pin.OUT_PP)  # 4 is the blue LED



# toggle LED state every second using on() and off() methods

while True:

  led.on()

  pyb.delay(1000)

  led.off()

  pyb.delay(1000)