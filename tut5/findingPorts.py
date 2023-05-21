import serial.tools.list_ports

def ListComPorts():
    i = 1
    for x in serial.tools.list_ports.comports():
        print('Option', i, '->', x)
        i+=1

if __name__ == '__main__':
    ListComPorts()