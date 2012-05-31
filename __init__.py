from Settings import Compile
from sys import stdout
from threading import Timer
import subprocess
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
from Modules import Calendar, i3, FancyTime 
TextModules={}
bars=[]
for screen in i3.getTree()["nodes"][1:]:
	bars.append(
			subprocess.Popen(
				('dzen2 ' + Compile(screen["rect"]["x"], screen["rect"]["width"]).options).split(" "), 
				shell=False, 
				stdin=subprocess.PIPE
			)
	)

def go():
	#Recieve outputs, compile, print.
	#for name,clas in TextModules.items():
	if not Settings.assist and len(TextModules) > 0:
		print([(name, x.output) for name, x in TextModules.items()])
		t=(Settings.preface+Settings.format.substitute(
			dict([(name, mod.output) for name, mod in TextModules.items()]))
		)
		#print(t)
		for bar in bars:
			bar.stdin.write(
				bytes(
					t + "\n",
					"UTF-8"
				)
			)

TextModules={
	Calendar.name:Calendar.display(go),
	i3.name:i3.display(go),
	FancyTime.name:FancyTime.display(go)
	}

if Settings.assist:
	print("Settings.format can use the following tags:")
	for Name,Module in TextModules.items():
		print("$" + str(Name))
		Module.Continue=False
	exit()
