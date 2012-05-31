import abstract
from datetime import datetime
import colours
name="fancytime"
def update(last):
	out = ""
	now = datetime.now()
	out =(str(now.day) + "th" if int(str(now.day)[-1]) >3 else str(now.day) + ["st","nd","rd"][int(str(now.day)[-1])-1]) +now.strftime(" of %B, %Y - ") + "^fg("+ colours.highlight.fg+")" + now.strftime("%I:%M%P") + "^fg()"
	return out
display=abstract.Module(1,update).display
