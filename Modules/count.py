#Example abstracted function
import abstract
#Name, will be used later in Settings.format as $name to use the output of this function
name="counter"
#Mandatory
display= abstract.Module(\
#The time between updates
3, \
#The function that is called on update, with the last value as input
lambda b: ((int(b)+1) if not b== '' else 0)\
#Mandatory
).display
