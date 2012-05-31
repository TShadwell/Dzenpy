#bindings for i3 functions, as well as a functional status bar
from os import popen
from json import loads
import abstract
import colours
name="i3"
def i3IPC(mesg):
	return loads(popen("i3-msg -t %s"%(mesg)).read())
def getWorkspaces():
	return i3IPC("get_workspaces")
def getOutputs():
	return i3IPC("get_outputs")
def getTree():
	return i3IPC("get_tree")
def getMarks():
	return i3IPC("get_marks")
def sendCommand(command):
	i3IPC("command %s" %(command))
def startProgram(name):
	sendCommand("exec %s" %name)
class workspace:
	def __init__(Self, JSON_workspace):
		j=JSON_workspace
		Self.name=j["name"]
		Self.urgent=j["urgent"]
		Self.visible=j["visible"]
		Self.focused=["focused"]
		Self.size=j["rect"]
	def __str__(Self):
		return Self.name
def processWorkspaces(rworkspaces):
	out =""
	workspaces=[(x.name,x) for x in [workspace(w) for w in rworkspaces]]
	return workspaces
def main(last):
	root = getTree()
	spaces=processWorkspaces(getWorkspaces())
	out = ""
	for screen in root["nodes"][1:]:
		out+=("[")
		for workspace in screen["nodes"][1]["nodes"]:
			out+=(workspace["name"]+"^") if workspace["name"] in dict([(name,g) for name, g in spaces if g.visible]) else (workspace["name"])
		out+=("]")
	return out
display= abstract.Module(
	1,
	main
).display
