import serial
import time
import statistics as stats

ser = serial.Serial('COM5', baudrate=115200, timeout=1)
encoding = 'ascii'
delay = 3
numPoints = 10
dataFile = open('dataFile.txt', 'w')
 

def getValues(input):
    ser.write(str(input).encode(encoding))
    data = ser.readline().decode(encoding)
    return data

time.sleep(delay) 
# this is done to make sure that we get user input only after
# after the arduino serial communication has been initialized

while True:
    userInput = input('Enter = ')
    XvalList, YvalList, SvalList = [], [], []
    if userInput == 'y': 
        for i in range(numPoints):
            data = getValues(userInput)
            dataFile.write(data)
            print(data:=[int(x) for x in data.split(',')])
            XvalList.append(data[0])
            YvalList.append(data[1])
            SvalList.append(data[2])

        print('Xmean =', stats.mean(XvalList))
        print('Xstdev =', stats.pstdev(XvalList))
        print('Ymean =', stats.mean(YvalList))
        print('Ystvdev =', stats.pstdev(YvalList))
    
    elif userInput == 'q':
        dataFile.close()
        exit(0)