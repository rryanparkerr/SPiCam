import picamera
import time

numberOfPhotos = 5

cam = picamera.PiCamera()
cam.resolution = (2700, 1800)

namePath = r"/home/pi/name.txt"
nameFile = open(namePath, "r")
cameraName = nameFile.readline()
nameFile.close()

for x in range(numberOfPhotos):
    time.sleep(5)
    imgPath = "/home/pi/" + cameraName + "_calibration" + str(x) + ".jpg"
    cam.capture(imgPath, format='jpeg', quality=100)
    print("image saved")

print('Done')
