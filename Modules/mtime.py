from threading import Timer
from datetime import datetime
from time import sleep
#Module displaying the time
name="time"
class display:
	def __init__(Self, fire):
		Self.fire = fire
		Self.t = Timer(0, Self.update)
		Self.t.start()
	output=""
	Continue=True

	def update(Self):
		if Self.Continue:
			Self.output = datetime.now().strftime("%H:%M:%S")
			Self.fire()
			sleep(1)
			Self.update()
		else:
			exit()
	#Async loop to update this.
	
