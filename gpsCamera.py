import os
import gpsd
import time
import datetime
import picamera
import clockUpdate as cu

# time.sleep(60)

fldrPath = r"/home/pi/Documents"
cameraName = "SPI_CAM" #Change this
logPath = os.path.join(fldrPath,cameraName+"_log.txt")

if not os.path.exists(logPath):
	log = open(logPath, "a")
	log.write("\"Event\" \"Date\" \"Time\" \"Lat./Long.\" \"File Path\"\r\n")
	log.close()

log = open(logPath, "a")
log.write("\"Pi booted (cpu time)\" "+str(datetime.datetime.now())+"\r\n")
log.close()

t = cu.updateClock()

log = open(logPath, "a")
log.write("\"Clock updated\" "+str(t)+"\r\n")
log.close()

gpsd.connect()
cam = picamera.PiCamera()
cam.resolution = (2700,1800)

fireTimes = []
gap = datetime.timedelta(microseconds=500000)
signal = True
gpsTime = 0
ready = False
shot = False

for h in range(24):
	window = [None]*2
	x = datetime.datetime(year=2, month=1, day=1, hour=h, minute=30)
	y = x+gap
	z = x-gap
	window[0] = y.time()
	window[1] = z.time()
	fireTimes.append(window)
print("All variables initialized")

while not ready:
	try:
		packet = gpsd.get_current()
		pos = packet.position()
		date = packet.get_time()
		ready = True
	except Exception:
		print("No signal")
		time.sleep(1)

log = open(logPath, "a")
log.write("\"Signal aquired\" "+str(date)+"\r\n")
log.close()

while True:
	received = False
	try:
		packet = gpsd.get_current()
		pos = packet.position()
		gpsTime = packet.get_time()
		received = True
		if not signal:
			log = open(logPath, "a")
			log.write("\"Signal restored\" "+str(gpsTime)+"\r\n")
			log.close()
		signal = True
	except Exception:
		if signal:
			if gpsTime == 0:
				log = open(logPath, "a")
				log.write("\"No signal - last ping\" "+str(date)+"\r\n")
				log.close()
			else:
				log = open(logPath, "a")
				log.write("\"No signal - last ping\" "+str(gpsTime)+"\r\n")
				log.close()
		signal = False
		print("No signal")

	if received == True:
		print("checking time "+str(gpsTime.time()))
		for i in range(len(fireTimes)):
			if fireTimes[i][0] > gpsTime.time() and fireTimes[i][1] < gpsTime.time():
				imgPath = os.path.join(fldrPath,cameraName+"_"+gpsTime.strftime("%Y%m%d_%H%M")+".jpg")
				print ("Firing camera and saving to "+str(imgPath))
				cam.capture(imgPath,format='jpeg',quality=100)
				log = open(logPath, "a")
				log.write("\"Photo taken\" "+str(gpsTime)+" \""+str(pos)+"\" "+str(imgPath)+"\r\n")
				log.close()

				print("this is when it shuts down")
				time.sleep(500)
				break
	time.sleep(.5)

