import abstract
from datetime import datetime
name="fancytime"
def update(last):
	out = ""
	now = datetime.now()
	out =(str(now.day) + "th" if int(str(now.day)[-1]) >3 else str(now.day) + ["st","nd","rd"][int(str(now.day)[-1])-1]) +now.strftime(" of %B, %Y - ") + "^fg(#FFFFFF)" + now.strftime("%I:%M%P") + "^fg()"
	return out
display=abstract.Module(1,update).display
