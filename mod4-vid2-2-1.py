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