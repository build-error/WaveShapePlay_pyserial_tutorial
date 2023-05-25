import time 
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def getValues(serCom, input, encodeFormat):
    serCom.write(str(input).encode(encodeFormat))
    return serCom.readline().decode(encodeFormat).rstrip()

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
    ax.axhline(y=500, color='red', linestyle='--', xmin=0, xmax=50)
    ax.set_ylim([0, 1024])
    ax.set_xlim([0, 50])
    ax.set_title("Xval data")
    ax.set_ylabel("Value")

    ay.clear()
    ay.plot(dataListY)
    ay.axhline(y=503, color='black', linestyle='--', xmin=0, xmax=50)
    ay.set_ylim([0, 1024])
    ay.set_xlim([0, 50])
    ay.set_title("Yval data")
    ay.set_ylabel("Value")

    ap.clear()
    ap.scatter(dataInt[0], dataInt[1])
    ap.axis('equal')
    ap.axhline(y=503, color='red', linestyle='--', xmin=0, xmax=1024)
    ap.axvline(x=500, color='black', linestyle='--', ymin=0, ymax=1024)
    ap.set_ylim([0, 1024])
    ap.set_xlim([0, 1024])
    ap.set_title("Pos data")
    ap.set_ylabel("Ypos")
    ap.set_xlabel("Xpos")

    fig.tight_layout()

if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=115200, timeout=1)

    time.sleep(3)

    dataListX, dataListY = [], []

    fig = plt.figure(figsize=(12, 4)) 
    gs = fig.add_gridspec(1, 3)  
    ax = fig.add_subplot(gs[0, 0])
    ay = fig.add_subplot(gs[0, 1])
    ap = fig.add_subplot(gs[0, 2])

    ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataListX, dataListY, ser, 'y', 'ascii'), interval=10)

    plt.show()
    ser.close()
