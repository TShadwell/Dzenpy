from Settings import Compile
from sys import stdout
from threading import Timer
import subprocess
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
from Modules import mtime, FancyTime 
TextModules={}
dzen = subprocess.Popen(('dzen2 '+Settings.options).split(" "), shell=False, stdin=subprocess.PIPE)

def go():
	#Recieve outputs, compile, print.
	#for name,clas in TextModules.items():
	if not Settings.assist and len(TextModules) > 0:
		dzen.stdin.write(bytes((Settings.format.substitute(dict([(name, mod.output) for name, mod in TextModules.items()]))) + "\n","UTF-8"))

TextModules={
	mtime.name:mtime.display(go),
	FancyTime.name:FancyTime.display(go,"right")
}

if Settings.assist:
	print("Settings.format can use the following tags:")
	for Name,Module in TextModules.items():
		print("$" + str(Name))
		Module.Continue=False
	exit()
