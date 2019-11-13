import os
#import gpsd
import time
import datetime


"""
gpsd.connect()
ready = False

while not ready:
    try:
	packet = gpsd.get_current()
	pos = packet.position()
	gpsTime = packet.get_time()
	ready = True
    except Exception:
	print("No signal")
    time.sleep(1)
"""
gpsTime = datetime.datetime(2019, 01, 01, 16, 15, 0)
acceptable = datetime.timedelta(seconds=1) 
cpuTime = datetime.datetime.now()

print(gpsTime)
print(cpuTime)
print("")

diff = abs(gpsTime-cpuTime)
print(diff)

if diff>acceptable:
	print("changing date")
	code = 'sudo timedatectl set-time \"'+str(gpsTime)+'\"'
	print(code)
	os.system(code)
	os.system('sudo hwclock -s')
print("done")
# return(gpsTime)
