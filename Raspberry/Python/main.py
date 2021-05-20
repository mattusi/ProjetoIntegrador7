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
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        center = "x: " + str(x - w/2) + "y: " + str(y + h/2)
        print(center)
	   	# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
		# draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        print(barcodeData)
        print(h)
        #TODO: Implement PID control for stoping
        if barcodeData == SequenceToFollow[nextStopIndex]:
            FollowLine(0)
            print("Currently at stop", SequenceToFollow[nextStopIndex])
            time.sleep(10.0)
            nextStopIndex = nextStopIndex + 1
            if nextStopIndex > len(SequenceToFollow):
                nextStopIndex = 0
            FollowLine(50)

		
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
	    break
# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
MotorsClose()