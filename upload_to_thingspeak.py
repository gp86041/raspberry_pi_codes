import httplib, urllib
from time import localtime, strftime
# download from http://code.google.com/p/psutil/
#import psutil
import time
from sense_hat import SenseHat

def doit():
	#cpu_pc = psutil.cpu_percent()
        sense=SenseHat()        
	cpu_temp = round(int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3,1)
        temph = sense.get_temperature_from_humidity()
        temphcali = temph - ((cpu_temp - temph)/1.5)
        
        tempp = sense.get_temperature_from_pressure()
        temppcali = tempp - ((cpu_temp - tempp)/1.5)
        
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
	params = urllib.urlencode({'field2': temphcali,'field3': temppcali,'field4': humidity,'field5': pressure,'key':'XXXXXXXXX'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print cpu_pc
		print mem_avail_mb
		print cpu_temp
		print strftime("%a, %d %b %Y %H:%M:%S", localtime())
		print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print "connection failed"	

#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
	while True:
		doit()
		time.sleep(60) 
