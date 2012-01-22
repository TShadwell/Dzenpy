from Settings import Compile
from sys import stdin
from threading import Timer
from io import UnsupportedOperation
Settings = Compile()
if Settings.debug:
	from datetime import datetime
	def dprint(string):
		now = datetime.now()
		if Settings.debug:
			print(now.strftime("[%H:%M:%S]: ") +string)
else:
	dprint = lambda a: a
dprint("Main started.")
import Modules
dprint("IMPORT ./Modules")
import Text
dprint("IMPORT ./Text")



dprint("dzen2 started.")
dprint("Entering main loop.")
Run = True
while Run:
	try:
		stdin.write("cool")
	except UnsupportedOperation:
		print(Text.NotPiping)
		Run = False