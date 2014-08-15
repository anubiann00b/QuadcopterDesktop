import sys
import serial

ser = serial.Serial(3)

while True:
    sys.stdout.write(ser.read())