#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

temp_C=input("hi there!\nwelcome to temperature converter\nplease provide the temperature in Celcius:\n")	#just learned, input function accepts only one argument (i tried to give two to achieve something like 32C)

try:
	temp_C_convtd=float(temp_C)
	counter=temp_C_convtd
except:
	counter=-1

if counter>=0:
	temp_F=temp_C_convtd*(9/5)+32
	print(temp_C_convtd,"Celcius is equivalent to",temp_F,"F")
elif counter<0:
	print('"',temp_C,'"',"is not a valid input, please provide Celcius temperature in numbers")


"""	output:
	
	Traceback (most recent call last):
	  File "/Users/pkewlani/Documents/py4e/textbook-ex2-5.py", line 3, in <module>
	    temp_C=input("hi there!\nwelcome to temperature converter\nplease provide the temperature in Celcius:\n","C")
	TypeError: input expected at most 1 argument, got 2

	hi there!
	welcome to temperature converter
	please provide the temperature in Celcius:

	C23
	23.0 Celcius is equivalent to 73.4 F

	hi there!
	welcome to temperature converter
	please provide the temperature in Celcius:
	23
	23.0 Celcius is equivalent to 73.4 F

	  File "/Users/pkewlani/Documents/py4e/textbook-ex2-5.py", line 3
	    temp_C=input("hi there!\nwelcome to temperature converter\nplease provide the temperature in Celcius:\n") print("C")	#just learned, input function accepts only one argument (i tried to give two to achieve something like 32C)
	                                                                                                              ^^^^^
	SyntaxError: invalid syntax

	hi there!
	welcome to temperature converter
	please provide the temperature in Celcius:
	32
	32.0 Celcius is equivalent to 89.6 F

	hi there!
	welcome to temperature converter
	please provide the temperature in Celcius:
	hundred
	hundred is not a valid input, please provide Celcius temperature in numbers

	hi there!
	welcome to temperature converter
	please provide the temperature in Celcius:
	hundred
	" hundred " is not a valid input, please provide Celcius temperature in numbers

"""