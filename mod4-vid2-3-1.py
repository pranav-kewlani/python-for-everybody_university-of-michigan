#problem stmnt: Europe floor count starts from 0 (Ground is 0) whereas US floor count starts from 1 (Ground is 1). here's a code to convert european floors to US floors.
eurofloor=input("provide European floor number (numbers only):\n")

#try block to check if floor number provided in int
try:
	usfloor=int(eurofloor)+1
	print ("please proceed to floor",usfloor,"in the US")

#except block to show message if user inpur is anything other than int
except:
	print ("please enter a valid floor number")


"""
output:
provide European floor number: 5.5
please enter a valid floor number

provide European floor number:3
please proceed to floor 4

provide European floor number:4
please proceed to floor 5 in the US

provide European floor number:five
please enter a valid floor number

provide European floor number (numbers only):4
please proceed to floor 5 in the US

"""