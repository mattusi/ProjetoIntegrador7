import serial

SPEED = 10
ser = serial.Serial('/dev/ttyS0')
currentLeftSpeed = 0
currentRightSpeed = 0


def MotorsSetup():
    ser.flushInput()
    ser.close()
    ser.open()
    
def L_Speed(speed):
    speed = abs(speed)
    if speed > 100:
        speed = 100
    currentLeftSpeed = speed
    sendCommand = str(currentLeftSpeed) + "a" + str(currentRightSpeed)
    print(sendCommand)
    ser.write(sendCommand.encode('ascii'))

def R_Speed(speed):
    speed = abs(speed)
    if speed > 100:
        speed = 100
    currentRightSpeed = speed
    sendCommand = str(currentLeftSpeed) + "a" + str(currentRightSpeed)
    print(sendCommand)
    ser.write(sendCommand.encode('ascii'))
    
def Direction(difference):
    difference /= 2
    L_Speed(SPEED + difference)
    R_Speed(SPEED - difference)

def BaseSpeed(speed):
    global SPEED
    SPEED = speed
    L_Speed(SPEED)
    R_Speed(SPEED)

def GetSpeed():
    global SPEED
    return SPEED

def MotorsStop():
    ser.write('0a0'.encode('ascii'))