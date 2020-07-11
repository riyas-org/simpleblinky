#self audio codec board
import machine
i2c = machine.I2C(scl=machine.Pin('PB10'), sda=machine.Pin('PB11'))
print('Scan i2c bus...')
print(i2c.scan()) #array

        