#RIYAS VETTUKATTIL
import pyb

led = pyb.Pin('LED', pyb.Pin.OUT_PP)  # 4 is the blue LED

# toggle LED state every second using on() and off() methods
def blink():
  #while True:
  for i in range(5):
    led.on()
    pyb.delay(1000)
    led.off()
    pyb.delay(1000)