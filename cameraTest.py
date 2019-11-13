import picamera
import time

cam = picamera.PiCamera()
cam.resolution = (2700,1800)
imgPath = "/home/pi/Documents/test.jpg"
time.sleep(5)
cam.capture(imgPath,format='jpeg',quality=100)

print('Done')
