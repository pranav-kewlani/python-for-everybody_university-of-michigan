#learning if statement and comparison operators

x=5

if x==5:
	print("x is 5")
if x>4:
	print("x is 5 or more")
if x>=5:
	print("x is still 5 or more")

if x<6:
	print("x is 5 or less")
if x <=5:
	print("x still 5 or less")
if x!=6:
	print("x is not 6")

	""" output:
	x is 5
	x is 5 or more
	x is still 5 or more
	x id 5 or less
	x still 5 or less
	x is not 6 """

#exploring if-else combo
	y=4
	if y>2:
		print("4 is larger than 2")
	else:
		print("2 is smaller than 4")

#exploring if-elif-else combo
z=10
if z<2:
	print("10 is lesser than 2")
elif z>2:
	print("10 larger than 2")
	if z>5:
		print("10 is larger than 5")	#this will be executed becuase its nested within an elif that will be executed
elif z>6:
	print("10 is larger than 6")	#this wont be executed because elif at line 38 is already executed
else:
	print("10 is between 2 & 100")
print ("all checked")

""" output:
10 larger than 2
all checked """
