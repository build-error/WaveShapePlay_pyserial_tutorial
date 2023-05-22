import serial
import time
import statistics as stats

ser = serial.Serial('COM5', baudrate=115200, timeout=1)
encoding = 'ascii'
delay = 3
numPoints = 10000
dataFile = open('dataFile.csv', 'w')
 

def getValues(serCom, input, encodeFormat):
    serCom.write(str(input).encode(encodeFormat))
    data = serCom.readline().decode(encodeFormat).rstrip()
    return data

def printToFile(serCom, file, encodeFormat, numPts):
    userInput = input('Enter = ')
    XvalList, YvalList, SvalList = [], [], []
    if userInput == 'y': 
        for i in range(numPts):
            data = getValues(serCom, userInput, encodeFormat)
            file.write(str(i) + ',' + data + '\n')
            print(data:=[int(x) for x in data.split(',')])
            XvalList.append(data[0])
            YvalList.append(data[1])
            SvalList.append(data[2])

        print('Xmean =', stats.mean(XvalList))
        print('Xstdev =', stats.pstdev(XvalList))
        print('Ymean =', stats.mean(YvalList))
        print('Ystvdev =', stats.pstdev(YvalList))
    
    elif userInput == 'q':
        file.close()
        return    

time.sleep(delay) 
# this is done to make sure that we get user input only after
# after the arduino serial communication has been initialized

if __name__ == "__main__":
    while True:
        printToFile(ser, dataFile, encoding, numPoints)
        break
