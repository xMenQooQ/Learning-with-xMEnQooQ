from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

c1 = (0, 0, 0)
c2 = (209, 35, 23)
leds = [
	c2, c1, c2, c1, c2, c2, c2, c1,
	c2, c2, c2, c1, c2, c1, c2, c1,
	c2, c1, c2, c1, c2, c2, c2, c1,
	c2, c1, c2, c1, c2, c1, c2, c1,
	c1, c1, c1, c1, c1, c1, c1, c1,
	c1, c1, c1, c1, c1, c1, c1, c1,
	c1, c1, c1, c1, c1, c1, c1, c1,
	c1, c1, c1, c1, c1, c1, c1, c1,
]
sense.set_pixels(leds)
sleep(2)