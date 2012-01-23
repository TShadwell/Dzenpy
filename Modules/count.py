import abstract
name="counter"
display=abstract.Module(3,lambda b: ((int(b)+1) if not b== '' else 0)).display
