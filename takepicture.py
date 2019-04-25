import numpy as np
import cv2
import time
import sys
import json


def set_camera():
	cam = cv2.VideoCapture(0)
	width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
	height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
	expo = cam.get(cv2.CAP_PROP_EXPOSURE)
	print ("default camera width is %d, height is %d, exposure is %f" % (width,height,expo))
	cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3264)
	cam.set(cv2.CAP_PROP_FRAME_HEIGHT,2448)
	cam.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.25)
	cam.set(cv2.CAP_PROP_EXPOSURE,0.6)   # 0.1, 0.05, 0.02
	cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))

	width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
	height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
	expo = cam.get(cv2.CAP_PROP_EXPOSURE)
	print ("test camera width is %d, height is %d, exposure is %f" % (width,height,expo))
	
	return cam


def read_config():
	return



reload(sys)
sys.setdefaultencoding("utf-8")

img_counter = 3
cam = set_camera()
time.sleep(3)

while img_counter:
	if cam.isOpened():
		ret, frame = cam.read()
		if not ret:
			break
		cv2.imwrite('/home/pi/Program/'+str(img_counter)+'.jpg', frame)
		print ("image file saved in /home/pi/Program/")
	
	time.sleep(2) #Sleep(2)
	img_counter = img_counter - 1

cam.release()
cv2.destroyAllWindows()