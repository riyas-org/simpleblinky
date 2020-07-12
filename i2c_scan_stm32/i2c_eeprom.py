from machine import I2C, Pin
i2c = I2C(scl=Pin('PB10'), sda=Pin('PB11'), freq=400000)
#i2c.writeto_mem(80, 0, 'test', addrsize=16)
data = i2c.readfrom_mem(80, 0, 4, addrsize=16)
