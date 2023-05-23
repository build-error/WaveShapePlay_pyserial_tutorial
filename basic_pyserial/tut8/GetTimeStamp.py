import serial
import time
import statistics as stats
from ini_read import getINI

iniData = getINI()

ser = serial.Serial('COM5', baudrate=115200, timeout=1)
encoding = iniData['encodeFormat']
delay = 3
numPoints = int(iniData['numPoints'])
dataFile = open(iniData['saveFile'], 'w')
 

def getValues(serCom, input, encodeFormat):
    serCom.write(str(input).encode(encodeFormat))
    data =  serCom.readline().decode(encodeFormat).rstrip()
    return data

def printToFile(serCom, file, encodeFormat, numPts):
    userInput = input('Enter = ')
    XvalList, YvalList, SvalList, TvalList = [0], [0], [0], [0]
    if userInput == 'c': 
        for i in range(numPts):
            data = getValues(serCom, userInput, encodeFormat)
            file.write(str(i) + ',' + data + '\n')
            print(data:=[int(x) for x in data.split(',')])
            XvalList.append(data[0])
            YvalList.append(data[1])
            SvalList.append(data[2])
            TvalList.append(data[3])

    elif userInput == 'g': 
        for i in range(numPts):
            data = getValues(serCom, userInput, encodeFormat)
            file.write(str(i) + ',' + data + '\n')
            print(data:=[int(x) for x in data.split(',')])
            XvalList.append(data[0])
            YvalList.append(data[1])
            SvalList.append(data[2])

    else:
        file.close()
        return 
       
    print('Xmean =', stats.mean(XvalList))
    print('Xstdev =', stats.pstdev(XvalList))
    print('Ymean =', stats.mean(YvalList))
    print('Ystvdev =', stats.pstdev(YvalList))
    

time.sleep(delay) 
# this is done to make sure that we get user input only after
# after the arduino serial communication has been initialized

if __name__ == "__main__":
    while True:
        # very slow code for some reason
        printToFile(ser, dataFile, encoding, numPoints)
        break
