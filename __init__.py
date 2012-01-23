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
TextModules={}
def go():
	#Recieve outputs, compile, print
	for name,clas in TextModules.items():
		print(clas.output)
TextModules={
	mtime.name:mtime.display(go)
}
if Settings.assist:
	print("Settings.format can use the following tags:")
	for Name,Module in TextModules.items():
		print("$" + str(Name))
		Module.Continue=False
	exit()