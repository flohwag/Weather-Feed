#!/bin/python
from weather import Weather
import time 
while True:
	print("Die aktuelle Uhrzeit")
	print(time.asctime())
	print("Das Wetter:")
	lookup = Weather.lookup(687154)
	condition = lookup.condition()
	print(condition['text'])
	time.sleep(90)
			
