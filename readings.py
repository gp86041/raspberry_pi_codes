##### Libraries #####
from datetime import datetime
from sense_hat import SenseHat
from time import sleep
from threading import Thread


##### Logging Settings #####
FILENAME = ""
WRITE_FREQUENCY = 1
TEMP_H=True
TEMP_P=True
HUMIDITY=True
PRESSURE=True
ORIENTATION=True
ACCELERATION=True
MAG=True
GYRO=True
DELAY=60

##### Functions #####
def file_setup(filename):
    header =[]
    if TEMP_H:
        header.append("temp_h")
    if TEMP_P:
        header.append("temp_p")
    if HUMIDITY:
        header.append("humidity")
    if PRESSURE:
        header.append("pressure")

    header.append("timestamp")

    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")

def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)


def get_sense_data():
    sense_data=[]

    if TEMP_H:
        sense_data.append(sense.get_temperature_from_humidity())

    if TEMP_P:
        sense_data.append(sense.get_temperature_from_pressure())

    if HUMIDITY:
        sense_data.append(sense.get_humidity())

    if PRESSURE:
        sense_data.append(sense.get_pressure())

    sense_data.append(datetime.now())

    return sense_data

def timed_log():
    while True:
        log_data()
        sleep(DELAY)




##### Main Program #####
sense = SenseHat()
batch_data= []

if FILENAME == "":
    filename = "SenseLog-"+str(datetime.now())+".csv"
else:
    filename = FILENAME+"-"+str(datetime.now())+".csv"

file_setup(filename)

if DELAY > 0:
    sense_data = get_sense_data()
    Thread(target= timed_log).start()

while True:
    sense_data = get_sense_data()

    if DELAY == 0:
        log_data()

    if len(batch_data) >= WRITE_FREQUENCY:
        print("Writing to file..")
        with open(filename,"a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []


    
