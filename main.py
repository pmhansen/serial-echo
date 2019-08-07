#!/usr/bin/python3

from datetime import datetime
import serial

SERIALPORT = '/dev/ttyUSB0'
BAUDRATE = 115200

ser = serial.Serial(SERIALPORT, BAUDRATE)
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE

ser.timeout = 1          # timeout block read

ser.xonxoff = False
ser.rtscts = True
ser.dsrdtr = False

ser.writeTimeout = 0

try:
    ser.close()
    ser.open()

except Exception as e:
    print('error open serial port: ' + str(e))
    exit()
    
if ser.isOpen():
    try:
        ser.flushInput()
        ser.flushOutput()

        while True:

            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

            print('TX: ' + dt_string)
            ser.write(dt_string.encode())

            rx = ser.readline()
            print('RX: ' + rx.decode("utf-8"))

        ser.close()

    except Exception as e:
        print('error communicating...: ' + str(e))

else:
    print('Y')