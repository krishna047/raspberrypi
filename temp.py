#!/usr/bin/python
from sense_hat import SenseHat
import time

ap = SenseHat()
temp = ap.get_temperature()
humidity = ap.get_humidity()
pressure = ap.get_pressure()


print("Temp: %s C" % temp)               # Show temp on console
print("Humidity: %s %%rH" % humidity)        # Show humidity on console
print("Pressure: %s Millibars" % pressure)    # Show pressure on console

ap.set_rotation(180)        # Set LED matrix to scroll from right to left
              
ap.show_message("%.1f C" % temp, scroll_speed=0.10, text_colour=[0, 255, 0])

time.sleep(1)           # Wait 1 second

ap.show_message("%.1f %%rH" % humidity, scroll_speed=0.10, text_colour=[255, 0, 0]) 

time.sleep(1)      # Wait 1 second

ap.show_message("%.1f Millibars" % humidity, scroll_speed=0.10, text_colour=[0, 0, 255])

ap.clear()      # Clear LED matrix
