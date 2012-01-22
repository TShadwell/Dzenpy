import Settings
if Settings.debug:
	from datetime import datetime
def dprint(string):
	now = datetime.now()
	if Settings.debug:
		print(now.strftime("[%H:%M:%S]: ") +string)
dprint("Main started.")
import Modules
dprint("IMPORT ./Modules")
import Clockwork
dprint("IMPORT ./Clockwork")