x=1+(((2**3)/4)*5) #same calculation but added parentheses to verify my unerstanding of operator precedence
y=x=1+2**3/4*5 #original numberical expression
print(x,y)

#output: 11.0 11.0

# trying floored int diviion (//) and modulus (%) operators
print ("trying floored division (//):", x//10)	#expected output: 1
print ("trying modulus operator(%):",y%3)	#expected output: 2

"""	output:
trying floored division (//): 1.0
trying modulus operator(%): 2.0
"""

#using the modulus operator to obtain the last digit(s) of the number
print ("the last digit in",x,"is",x%10)
print ("the last two digits in",x,"are",x%100)
#realised, modulus can also be used to identify the number of digits in a number
print ("the last three digits in",x,"are",x%1000) #unable to formulate the logic as of now, but when the result of the modulus operation shows digits less than the number of 0s, the number of digits in the number = number of (0s - 1)

"""	output:
the last digit in 11.0 is 1.0
the last two digits in 11.0 are 11.0
the last three digits in 11.0 are 11.0
"""

#using the + and * operators with strings

first = "test"
sec = 3
thir = "ing"
print ("first*sec =",first*sec)
print("first+sec =",first+thir)

"""	output:
first*sec = testtesttest
first+sec = testing
"""