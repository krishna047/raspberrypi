from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)
sense.show_letter("D",text_colour=[255, 0, 0])
time.sleep(1)
sense.show_letter("o",text_colour=[0, 0, 255])
time.sleep(1)
sense.show_letter("n",text_colour=[0, 255, 0])
time.sleep(1)
sense.show_letter("a",text_colour=[0, 0, 0], back_colour=[255, 255, 255])
time.sleep(1)
sense.clear()
