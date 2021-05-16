#include <FalconRobot.h>

// initialize a sensor object on A2 and A3
FalconRobotLineSensor left(A1);
FalconRobotLineSensor right(A2);

FalconRobotMotors motors(5, 7, 6, 8);
int leftPower;  // variable for setting the drive power
int rightPower; // variable for setting the drive power
int leftDirection; // variable for setting the direction
int rightDirection; // variable for setting the direction
const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data

int moveInts[2];
boolean newData = false;
boolean keepFolloingLine = false;
int SPEED; 

int leftValue;  // variable to store the left sensor value
int rightValue;  // variable to store the right sensor value

int leftSpeed;  // variable used to store the leftMotor speed
int rightSpeed;  // variable used to store the rightMotor speed

#define LINETHRESHOLD 900
#define Kp 0.129

float error;
int direct; 

void setup(void) {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop(void) {
  // if there is data coming in on the Serial monitor, do something with it.
  recvWithEndMarker();
  if (newData == true) {
    if (strstr(receivedChars, "L")) {
      updateSpeed(receivedChars);
      
      keepFolloingLine = true;
      Serial.println("Folloing line");
    } else {
      keepFolloingLine = false;
      processString("-", receivedChars);
      moveBySerial(moveInts[0], moveInts[1]);
    }
    newData = false;
  }
  followLine();
}

void recvWithEndMarker() {
    static byte ndx = 0;
    char endMarker = '\n';
    char rc;
    
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (rc != endMarker) {
            receivedChars[ndx] = rc;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; // terminate the string
            ndx = 0;
            newData = true;
        }
    }
}

void moveBySerial(int left, int right) {
  Serial.println("Should move by serial");
  leftPower = left; // read in the next numeric value (NEEDS OPTIMIZATION)
  Serial.print(leftPower);
  leftPower = constrain(leftPower, -100, 100);  // constrain the data to -100 to +100

  rightPower = right;   // read in the next numeric value
  Serial.println(rightPower);  
  rightPower = constrain(rightPower, -100, 100);  // constrain the data to -100 to +100


    // set the direction by the signal of the speed
    if (leftPower < 0) {
      leftPower = - leftPower;
      leftDirection = BACKWARD;
    }
    else {
      leftDirection = FORWARD;
    }

    // set the direction by the signal of the speed
    if (rightPower < 0) {
      rightPower = - rightPower;
      rightDirection = BACKWARD;
    }
    else {
      rightDirection = FORWARD;
    }

    // set motors
    motors.leftDrive(leftPower, leftDirection);
    motors.rightDrive(rightPower, rightDirection);

}

void followLine(void) {
  if (keepFolloingLine) {
    // Read the sensors
    leftValue = left.read();
    rightValue = right.read();
    error = leftValue - rightValue - 6;
  
    // Print the sensors values
    //Serial.print(leftValue);
    //Serial.print("\t");  // tab character
    //Serial.print(rightValue);
    //Serial.print("\t");
    //Serial.print(error);
    //Serial.println();   // new line
  
  
    direct = error * Kp;
    leftSpeed = SPEED - direct;
    rightSpeed = SPEED + direct;
    // run motors given the control speeds above
    motors.leftDrive(leftSpeed, FORWARD);
    motors.rightDrive(rightSpeed, FORWARD);
  
    delay(0);  // add a delay to decrease sensitivity.
  }
}

void updateSpeed(char* data) {
  char* d = strtok(data, "-");
  int i = 0;
  while (d != NULL) {
    Serial.println(d);
    int moveSpeedInt = atoi(d);
    SPEED = moveSpeedInt;
    i++;
    d = strtok(NULL, "-");
    }
  Serial.println(SPEED);
  
}

void processString(char* delimiter, char* data){
    Serial.println(data);
    char* d = strtok(data, "-");
    int i = 0;
    while (d != NULL) {
      Serial.println(d);
      int moveSpeedInt = atoi(d);
      moveInts[i] = moveSpeedInt;
      i++;
      d = strtok(NULL, "-");
    }
}
