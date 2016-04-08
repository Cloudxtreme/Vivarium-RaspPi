import os
import glob
import time

#load the kernel modules needed to handle the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


#finds the path of a sesor directory that starts with 28
devicelist = glob.glob('/sys/bus/w1/devices/28*')
#append the device file name to get the absolute path of the sensor
devicefile = devicelist[0] + '/w1_slave'

#open the file representing the sensor
def get_temp(devicefile)
    try:
        fileobj = open(devicefile, 'r')
        lines = fileobj.readlines()
        fileobj.close()
    except:
        return None

        #get the status from the end of line 1
        status = lines[0][-4:-1]

        #checks if the status is okay
        if status=="YES":
            print status
            tempstr= lines[1][-6:-1]
            tempvalue=float(tempstr)/1000
            print "The temperature was" + tempvalue + "degrees celsius."
            else
            print "There was an error"
            return None
