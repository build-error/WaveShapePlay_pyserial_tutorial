import time 
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import statistics as stats

def getValues(serCom, input, encodeFormat):
    serCom.write(str(input).encode(encodeFormat))
    data =  serCom.readline().decode(encodeFormat).rstrip()
    return data

def animateX(i, dataListX, ser, userInput, encoding):
    dataString = getValues(ser, userInput, encoding)
    
    try:
        dataInt = [int(x) for x in dataString.split(',')]
        dataListX.append(dataInt[0])

    except:
        pass

    dataListX = dataListX[-50:]

    ax.clear()
    ax.plot(dataListX)

    ax.set_ylim([0, 1023])
    ax.set_title("Xval data")
    ax.set_ylabel("Value")

if __name__ == '__main__':
    ser = serial.Serial('COM5', baudrate=115200, timeout=1)

    time.sleep(3)

    dataListX = []

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ani = animation.FuncAnimation(fig, animateX, frames=100, fargs=(dataListX, ser, 'y', 'ascii'), interval=10)
    plt.show()
    ser.close()