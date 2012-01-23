from threading import Timer
from datetime import datetime
from time import sleep
#Module displaying the time
class Module:
	def __init__(Self, Timeout, updateproc):
		Self.display.Timeout= Timeout
		Self.display.updateproc = lambda Self, x: updateproc(x)
	class display:
		def __init__(Self, fire):
			Self.fire = fire
			Self.t = Timer(0, Self.update)
			Self.t.start()
		output=""
		Continue=True
		Timeout = 0
		def update(Self):
			if Self.Continue:
				Self.output = Self.updateproc(Self.output)
				Self.fire()
				sleep(Self.Timeout)
				Self.update()
			else:
				exit()
	
