import serial
try:
    ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
except:
    ser=serial.Serial('/dev/ttyACM1',9600,timeout=1)
while True:
    angle=135
    speed=255
    sendData=f"{angle},{speed}\n"
    arr = bytes(sendData, 'utf-8')
    ser.write(arr)

    