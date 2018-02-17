import time
import serial
import string
import pynmea2
import RPi GPIO as gpio

gpio.setmode(gpio.BCM)
 
sleepTime = 0
port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
 
#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
 
def Gps_loc():
    try:
        data = ser.readline()
    except:
		print("loading") 

    if data[0:6] == '$GPGGA': # the long and lat data are always contained in the GPGGA string of the NMEA data
 
        msg = pynmea2.parse(data)
 
        latval = msg.lat
		concatlat = "lat:" + str(latval)
        print concatlat

		longval = msg.lon
		concatlong = "long:"+ str(longval)
		print concatlong
    
    location = (latval, longval)
    time.sleep(sleepTime)
    return location