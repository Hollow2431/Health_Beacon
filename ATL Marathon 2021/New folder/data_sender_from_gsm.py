# import RPi.GPIO as GPIO
import serial
import time, sys

SERIAL_PORT = "/dev/ttys0"
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)

# Commands
"""
AT+CGATT=1 --> attaches GPRS
AT+CIPMUX=0 --> enables single IP connection
AT+CSTT="APN",username,password --> set the APN, username and password
AT+CIICR --> starts wireless connection
AT+CIFSR --> returns the IP allotted by GPRS
AT+CIPSTART="TCP","IP","Port server is running on" --> Establish connection with the server
AT+CIPSEND
Your messaage$1A
"""
ser.write()
