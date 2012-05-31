from string import Template
import colours
class Compile:
	def __init__(Self,x=0, width=0):
		dzen2={
			#X position of the bar
			"x":x,
			#Y
			"y":0,
			#If it is placed in the WM's dock
			"dock":"",
			#Events
			"e":"\'\'",
			#Height
			"h":10,
			#Width
			"w":0,
			#Font
			"fn":"glisp",
			#Text Colour
			"fg":colours.primary.fg,
			#Background colour
			"bg":colours.primary.bg,
			#Align
			"ta":"l"
		}
		format = "$fancytime"
		Self.format = Template(format)
		Self.options=''.join(["-%s%s " %(prop,(" " + str(val) if not str(val) == "" else "")) for prop, val in dzen2.items()]).strip(" ")
		del dzen2
	preface=""
	debug = False
	assist = False
	
