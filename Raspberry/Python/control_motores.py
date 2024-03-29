import serial

SPEED = 10
ser = serial.Serial('/dev/ttyS0', 9600)
currentLeftSpeed = 0
currentRightSpeed = 0


def MotorsSetup():
    ser.flushInput()
    ser.close()
    ser.open()

def MotorsClose():
    ser.close()
    
def L_Speed(speed):
    global currentRightSpeed
    global currentLeftSpeed
    speed = abs(speed)
    if speed > 100:
        speed = 100
    currentLeftSpeed = speed
    sendCommand()

def R_Speed(speed):
    global currentRightSpeed
    global currentLeftSpeed
    speed = abs(speed)
    if speed > 100:
        speed = 100
    currentRightSpeed = speed
    sendCommand()
    
    
def Direction(difference):
    global currentRightSpeed
    global currentLeftSpeed
    difference /= 2
    currentLeftSpeed = SPEED + difference
    currentRightSpeed = SPEED - difference
    sendCommand()

def BaseSpeed(speed):
    global SPEED
    global currentRightSpeed
    global currentLeftSpeed
    SPEED = speed
    currentRightSpeed = speed
    currentLeftSpeed = speed
    sendCommand()

def FollowLine(Speed):
    sendCommand = "L-" + str(Speed)
    print(sendCommand)
    ser.write((sendCommand + '\r\n').encode())


def GetSpeed():
    global SPEED
    return SPEED

def MotorsStop():
    ser.write('0-0'.encode('ascii'))

def sendCommand():
    global currentRightSpeed
    global currentLeftSpeed
    leftInt = int(currentLeftSpeed)
    rightInt = int(currentRightSpeed)
    sendCommand = str(leftInt) + "-" + str(rightInt)
    print(sendCommand)
    ser.write((sendCommand + '\r\n').encode())