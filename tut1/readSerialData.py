import serial

ser = serial.Serial('COM4', baudrate=9600, timeout=1)

while True:
    data = ser.readline().decode('ascii')
    print(data)