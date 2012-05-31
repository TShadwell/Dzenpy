from threading import Timer
from datetime import datetime
from time import sleep
#Module displaying the time

class Module:
	def __init__(Self, Timeout, updateproc):
		Self.display.Timeout= Timeout
		Self.display.updateproc = lambda Self, x: updateproc(x)
	class display:
		align = lambda *a:a[1]
		def __init__(Self, fire, align="default"):
			Self.fire = fire
			Self.output=""
			Self.t = Timer(0, Self.update)
			Self.t.start()
			if align=="default":
				pass
			elif align=="left":
				Self.align=lambda a: "^p(_LEFT)^p(%s)"%((len(''.join([m for m in [x.split("^")[0] for x in a.split(")")] if not m=='']))+1) * 6) + a + "^p()"
			elif align=="right":
				Self.align=lambda a: "^p(_RIGHT)^p(-%s)"%((len(''.join([m for m in [x.split("^")[0] for x in a.split(")")] if not m=='']))+1) * 6) + a + "^p()"
			else:
				print("Invalid alignment \"%s\"."%(align))
		Continue=True
		Timeout = 0
		def update(Self):
			if Self.Continue:
				Self.output = Self.align(Self.updateproc(Self.output))
				Self.fire()
				sleep(Self.Timeout)
				Self.update()
			else:
				exit()
	
