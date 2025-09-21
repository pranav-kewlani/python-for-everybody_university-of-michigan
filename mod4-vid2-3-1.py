#problem stmnt: Europe floor count starts from 0 (Ground is 0) whereas US floor count starts from 1 (Ground is 1). here's a code to convert european floors to US floors.
eurofloor=input("provide European floor number (numbers only):")

#try block to check if floor number provided in int
try:
	usfloor=int(eurofloor)+1
	print ("please proceed to floor",usfloor,"in the US")

#except block to show message if user inpur is anything other than int
except:
	print ("please enter a valid floor number")


"""
output:

"""