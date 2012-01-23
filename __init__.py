from Settings import Compile
from sys import stdout
from threading import Timer
import Text
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
from Modules import mtime

dprint("IMPORT ./Text")
dprint("dzen2 started.")
dprint("Entering main loop.")
TextModules={}
def go():
	#Recieve outputs, compile, print
	for name,clas in TextModules.items():
		print(clas.output)
TextModules={
	"time":mtime.display(go)
}
