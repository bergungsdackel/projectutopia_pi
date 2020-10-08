import smbus
import math


def init_gyro():
    # Register
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect, Addresse rausfinden!

    # Aktivieren, um das Modul ansprechen zu koennen
    bus.write_byte_data(address, power_mgmt_1, 0)


#Methoden
def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


#Werte, die man tatsächlich braucht
def read_gyro():
    gyroskop_x = read_word_2c(0x43)
    gyroskop_y = read_word_2c(0x45)
    gyroskop_z = read_word_2c(0x47)

    gyroskop_x_skaliert = gyroskop_x / 131
    gyroskop_y_skaliert = gyroskop_y / 131
    gyroskop_z_skaliert = gyroskop_z / 131

    beschleunigung_x = read_word_2c(0x3b)
    beschleunigung_y = read_word_2c(0x3d)
    beschleunigung_z = read_word_2c(0x3f)
 
    beschleunigung_x_skaliert = beschleunigung_x / 16384.0
    beschleunigung_y_skaliert = beschleunigung_y / 16384.0
    beschleunigung_z_skaliert = beschleunigung_z / 16384.0

    x_rotation = get_x_rotation(beschleunigung_x_skaliert, beschleunigung_y_skaliert, beschleunigung_z_skaliert)
    y_rotation = get_y_rotation(beschleunigung_x_skaliert, beschleunigung_y_skaliert, beschleunigung_z_skaliert)