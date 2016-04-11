import os
import glob
import time
import sys
import Adafruit_Python_DHT

#git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#cd Adafruit_Python_DHT
sensor_args = { '11': Adafruit_DHT.DHT11,
                                    '22':Adafruit_DHT.DHT22,
                                    '2302': Adafruit_DHT.AM2302}
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
        sensor = sensor_args[sys.argv[1]]
        pin = sys.argv[2]
else:
        print 'usage: sudo ./Adafruit.DHT.py [11|22|2302] GPIOpin#'
        print 'example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 ceonnected to GPIO #4'

#Tries to grab the measurements again (15 times) every 2 seconds

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
temperature = temperature * 9/5.0 + 32
if humidity is not None and temperature is not None:
        print 'Temp={0:0.1f}* Humidity={1:0.1f}%'.format(temperature, humidity)
else:
        print 'Failed to get reading. Try again!'
        sys.exit(1)
#store the temperature in the database

def log_temperature(temperature, humidity):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    #inserts the temperature and humidity into the tables
    curs.execute("INERT INTO temps values(datetime('now'), (?))", (temperature))
    curs.execute("INERT INTO humid values(datetime('now'), (?))", (humidity))
    #commit the changes
    conn.commit()

    conn.close()
