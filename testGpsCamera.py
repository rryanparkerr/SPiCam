import os
#import gpsd
import time
import datetime
import picamera


time.sleep(60)

fldrPath = r"/home/pi/Documents"
cameraName = "TESTER"
"""
logPath = os.path.join(fldrPath,cameraName+"_log.txt")

if not os.path.exists(logPath):
	log = open(logPath, "a")
	log.write("\"Event\" \"Date\" \"Time\" \"Lat./Long.\" \"File Path\"\r\n")
	log.close()

log = open(logPath, "a")
log.write("\"Pi booted (cpu time)\" "+str(datetime.datetime.now())+"\r\n")
log.close()

gpsd.connect()
"""
cam = picamera.PiCamera()
cam.resolution = (2700,1800)

gpsTime = 0

while True:
	"""
	received = False
	try:
		packet = gpsd.get_current()
		pos = packet.position()
		gpsTime = packet.get_time()
		received = True
	except Exception:
		gpsTime = datetime.datetime.now()
		print("No signal")
	"""

	gpsTime = datetime.datetime.now() #comment out if using log
	imgPath = os.path.join(fldrPath,cameraName+"_"+gpsTime.strftime("%Y%m%d_%H%M%S")+".jpg")
	print ("Firing camera and saving to "+str(imgPath))
	cam.capture(imgPath,format='jpeg',quality=100)
	"""
	if received:
		log = open(logPath, "a")
		log.write("\"Photo taken\" "+str(gpsTime)+" \""+str(pos)+"\" "+str(imgPath)+"\r\n")
		log.close()
	else:
		log = open(logPath, "a")
		log.write("\"Photo taken (cpu time)\" "+str(gpsTime)+" \""+"NO SIGNAL"+"\" "+str(imgPath)+"\r\n")
		log.close()
	"""

	time.sleep(5)


