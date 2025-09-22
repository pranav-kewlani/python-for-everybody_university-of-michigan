#demo of the basic level ideal usage of the try-except logic

userinput=input("enter a positive number only ")

try:
	conv= float(userinput)
except:
	conv= -1	#catches the traceback but does not stop the user feedback

#now the user is given a result/feedback based on the input

if conv>0:
	print("nice work, providing",conv,"as input")	#result if the user gives a posotive number as input
else:
	print("not a positive number")	#feedback if user gives anything other than a positive number (text, -ve number, etc)

#in either cases, even if the user provides an unexpected input, the feedback is ensured.


"""	output
	for input= 3
		enter a positive number only 3
		nice work, providing 3.0 as input
	for input= three
		enter a positive number only three
		not a positive number
"""