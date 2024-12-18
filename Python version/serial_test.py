import time

import serial

ser = serial.Serial ('COM5', 9600)

ser.write (b'e')
time.sleep (2)
ser.write (b'f')


ser.close ()
