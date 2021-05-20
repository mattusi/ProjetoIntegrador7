from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

from control_motores import *

SequenceToFollow = ["A", "C", "B"]
Speed = 50

MotorsSetup()
BaseSpeed(Speed)

print(cv2.__version__) #check if cv2 is installed 

print("[INFO] Starting video stream...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

nextStopIndex = 0
time.sleep(5.0)
FollowLine(50)
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    barcodes = pyzbar.decode(frame)

    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
	   	# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        
        print(barcodeData)
        print(h)
        #TODO: Implement PID control for stoping
        if barcodeData == SequenceToFollow[nextStopIndex]:
            if h > 90:
                FollowLine(0)
                print("Currently at stop", SequenceToFollow[nextStopIndex])
                time.sleep(10.0)
                nextStopIndex = nextStopIndex + 1
                if nextStopIndex > len(SequenceToFollow):
                    nextStopIndex = 0
                FollowLine(50)

    key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
	    break
# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
MotorsClose()