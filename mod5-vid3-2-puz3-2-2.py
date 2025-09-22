#puzzle statement: identify which line will not be executed irrespective of the value of x

x=input("provide an integer/float value for x: ")

if float(x)<2:
	print("value is below 2")
elif float(x)<20:
	print("value is below 20")
elif float(x)<10:	#this will be exempted from execution because anything less than 10 will also be less than 20 & because elif at line 7 will be executed for all x<20
	print("value is below 10")
else:	#thought this might be the one that would be skipped but it can be executed if x>20
	print("something else")

"""	output:
	for x=3:
		provide an integer/float value for x: 3
		value is below 20
	for x-45:
		provide an integer/float value for x: 45
		something else
"""