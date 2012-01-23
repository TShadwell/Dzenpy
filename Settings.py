from string import Template
class Compile:
	def __init__(Self):
		dzen2={
			#X position of the bar
			"x":0,
			#Y
			"y":0,
			#If it is placed in the WM's dock
			"dock":"",
			#Events
			"e":"\'\'",
			#Height
			"h":20,
			#Width
			"w":2880,
			#Font
			"fn":"drift.se",
			#Text Colour
			"fg":"#575757",
			#Background colour
			"bg":"#282828",
			#Align
			"ta":"l"
		}
		format = "Current time: $time Test: $counter"
		Self.format = Template(format)
		Self.options=''.join(["-%s%s " %(prop,(" " + str(val) if not str(val) == "" else "")) for prop, val in dzen2.items()]).strip(" ")
		del dzen2
	debug = False
	assist = False
	
