#puzzle statement: identify which line will not be executed irrespective of the value of x

x=input("provide an integer/float value for x: ")

if float(x)<2:
	print("x is less than 2")
elif float(x)>=2:
	print("x is larger than/equal to 2")
else:
	print("2 is not a number")	#this will not be executed because either of the 2 above will be executed as long as x holds any int/float value irrespective of the value itself

	"""	output:
	for x = 4:
		provide an integer/float value for x 4
		x is larger than/equal to 2
	for x = 1:
		provide an integer/float value for x 1
		x is less than 2	"""