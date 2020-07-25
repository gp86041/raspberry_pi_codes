import os,time, datetime
from datetime import timedelta
from sense_hat import SenseHat
# enter target time and date here

day=30
month=6
year=2017
hour=0
minutes=0
sec=0
targetTime = datetime.datetime(year, month, day, hour, minutes) # sets up target time
timeNow =datetime.datetime.now()


remainingTime=(targetTime-timeNow)
days = remainingTime.days
secs = remainingTime.seconds
hrs, secs = divmod(secs, 3600)
mins, secs = divmod(secs, 60)

#############################

OFFSET_LEFT = 1
OFFSET_TOP = 1

NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# Displays a single digit (0-9)
def show_digit(val, xd, yd, r, g, b):
  offset = val * 15
  for p in range(offset, offset + 15):
    xt = p % 3
    yt = (p-offset) // 3
    sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

# Displays a two-digits positive number (0-99)
def show_number(val, r, g, b):
  abs_val = abs(val)
  tens = abs_val // 10
  units = abs_val % 10
  if (abs_val > 9):
      show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
  show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)


################################################################################
# MAIN

sense = SenseHat()
sense.clear()

if days <= 9:
    sense.show_letter(str(days),[255,0,0])
else:
    show_number(days, 0, 255, 0)
        
    

