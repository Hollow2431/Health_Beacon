import RPi.GPIO as GPIO
import serial
import time, sys

SERIAL_PORT = "/dev/ttys0"
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)