# verify the lenght of 'main.py'
with open('main.py', 'r') as file:
	l = len(file.read())
	print(l <= 560)
	print(l)
