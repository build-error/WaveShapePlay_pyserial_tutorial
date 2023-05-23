import serial
import time

ser = serial.Serial('COM4', baudrate=9600, timeout=1)
encoding = 'ascii'
delay = 3

def getValues(input):
    ser.write(str(input).encode(encoding))
    data = ser.readline().decode(encoding)
    return data


time.sleep(delay) 
# this is done to make sure that we get user input only after
# after the arduino serial communication has been initialized

while True:
    userInput = input('Enter = ')
    if userInput == 'y': print(getValues(userInput))