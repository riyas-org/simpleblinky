# main.py -- put your code here!
#RIYAS VETTUKATTIL
import pyb
from pyb import Timer

led = pyb.Pin('PG14', pyb.Pin.OUT_PP)  # 4 is the blue LED

# toggle LED state every second using on() and off() methods
k=0

while True:
#  led.on()
  pyb.delay(5)
#  led.off()
  pyb.delay(5)
  fade = pyb.Pin('PB10', pyb.Pin.OUT_PP)  # 4 is the blue LED
  tim = Timer(2, freq=1000)
  ch = tim.channel(3, Timer.PWM, pin=fade )
  ch.pulse_width_percent(abs(k))
  if(k==0):
    pyb.delay(1000);  
  k=k+1
  if(k==100):    
    led.on()
    pyb.delay(200)
    led.off() 
    k=-100  

  
