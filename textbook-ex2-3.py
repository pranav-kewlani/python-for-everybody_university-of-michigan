# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.


hrs=input("hey there! please provide your total working hours:\n")
rate=input("please also share your current hourly wage:\n $")

try:
	hrs_convtd= float(hrs) #try if working hrs are int/float
	counter1=hrs_convtd	#made a mistake here, took hrs instead of hrs_convtd, which generated traceback as counter1 was assigned value -1

	if counter1>=0:	#proceed only if working hrs are int/float
		try:
			rate_convtd=float(rate)	#if working hrs are int/float, try if rate is in int/float
			counter2=rate_convtd
		except:
			counter2=-1

except:
	counter1=-1


if counter1>=0:	
	print("calculating pay for",hrs_convtd,"hours worked...")
	if counter2>=0:
		print("total pay as per $",rate_convtd,"per hour = $",hrs_convtd*rate_convtd)
	elif counter2<0:
		print(rate,"is not a valid input, please provide rate in numbers")	#made a mistake here, took the variable rate_convtd instead of rate
elif counter1<0:
	print(hrs,"is not a valid input, please provide hours in numbers")	#made a mistake here, took the variable hrs_convtd instead of hrs, got a traceback


"""	output:
	hey there! please provide your total working hours:
	five
	please also share your current hourly wage:
	 $20.5
	five is not a valid input, please provide hours in numbers

	hey there! please provide your total working hours:
	5
	please also share your current hourly wage:
	 $20.5
	counter1= -1
	5 is not a valid input, please provide hours in numbers
	
	hey there! please provide your total working hours:
	5
	please also share your current hourly wage:
	 $20.5
	calculating pay for 5.0 hours worked...
	total pay as per $ 20.5 per hour = $ 102.5
	
	hey there! please provide your total working hours:
	0
	please also share your current hourly wage:
	 $20.5
	calculating pay for 0.0 hours worked...
	total pay as per $ 20.5 per hour = $ 0.0
	
	hey there! please provide your total working hours:
	4
	please also share your current hourly wage:
	 $ten.5
	calculating pay for 4.0 hours worked...
	ten.5 is not a valid input, please provide rate in numbers
	
"""