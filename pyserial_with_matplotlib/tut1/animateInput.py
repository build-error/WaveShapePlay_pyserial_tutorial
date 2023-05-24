import time 
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def getValues(serCom, input, encodeFormat):
    serCom.write(str(input).encode(encodeFormat))
    data =  serCom.readline().decode(encodeFormat).rstrip()
    return data

def animate(i, dataListX, dataListY, ser, userInput, encoding):
    dataString = getValues(ser, userInput, encoding)
    print(dataString)

    try:
        dataInt = [int(x) for x in dataString.split(',')]
        dataListX.append(dataInt[0])
        dataListY.append(dataInt[1])

    except:
        pass

    dataListX = dataListX[-50:]
    dataListY = dataListY[-50:]

    ax.clear()
    ax.plot(dataListX)
    ax.set_ylim([0, 1050])
    ax.set_title("Xval data")
    ax.set_ylabel("Value")

    ay.clear()
    ay.plot(dataListY)
    ay.set_ylim([0, 1050])
    ay.set_title("Yval data")
    ay.set_ylabel("Value")


if __name__ == '__main__':
    ser = serial.Serial('COM5', baudrate=115200, timeout=1)

    time.sleep(3)

    dataListX, dataListY = [], []

    # fig, (ax, ay) = plt.subplots(2,1)
    fig = plt.figure(tight_layout=True)
    (ax, ay) = fig.subplots(2,1)

    aniX = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataListX, dataListY, ser, 'y', 'ascii'), interval=10)

    plt.show()
    ser.close()