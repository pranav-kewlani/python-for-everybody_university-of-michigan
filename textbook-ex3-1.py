#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#rewriting original logic first:
hours=input("please provide your working hours in numbers only:\n")
rate=input("please provide your current rate per hour in numbers only:\n$")

try:
	hours_convtd=float(hours)	#forgot to change variable name
	counter1=hours_convtd #forgot to change variable name
	try:
		rate_convtd=float(rate)
		counter2=rate_convtd
	except:
		counter2=-1

except:
	counter1=-1

if counter1>=0:
	if counter2>=0:	
		if hours_convtd>40:	#1.5x the pay if hrs>40
			print("whoa! you just unlocked 1.5x pay!! \nkeep working 40+ hrs to keep up this momentum!")
			print("calulating pay for",hours_convtd,"hours as per $",rate_convtd,"/ hour...")	#changed "per hour" to "/hour"
			print("your actual pay totals to: $",hours_convtd*rate_convtd,"BUT")
			print("working 40+ hrs just earned you $",hours_convtd*1.5*rate_convtd,"!")
		elif 30<hours_convtd<40: #boosting the user if he/she alredy worked 30+hrs
			print("calulating pay for",hours_convtd,"hours as per $",rate_convtd,"/ hour...")	#changed "per hour" to "/hour"
			print("hey! did you know you're just",40-hours_convtd,"hrs away from earning 1.5x your pay!\nput in a bit more in next time and take the jackpot!")	#used wrong variable name here
			print("your current pay totals to $",hours_convtd*rate_convtd)
		else:
			print("calulating pay for",hours_convtd,"hours as per $",rate_convtd,"/ hour...")	#changed "per hour" to "/hour"
			print("your pay totals to $",hours_convtd*rate_convtd)
	else:
		print('"',rate,'"',"is not a valid input :( , please provide the rate in numbers")
else:
	print('"',hours,'"',"is not a valid input :( , please provide the hours worked in numbers")


"""	output:
File "/Users/pkewlani/Documents/py4e/textbook-ex3-1.py", line 24
    			print("your actual pay totals to: $"hours_convtd*rate_convtd,"BUT")
    			      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

  File "/Users/pkewlani/Documents/py4e/textbook-ex3-1.py", line 36
    	print('"',hours'"',"is not a valid input:(, please provide the hours worked in numbers")
    	               ^^^
SyntaxError: invalid syntax

please provide your working hours in numbers only:
	forty one
please provide your current rate per hour in numbers only:
	$32.6
	" forty one " is not a valid input:(, please provide the hours worked in numbers

please provide your working hours in numbers only:
	36.4
please provide your current rate per hour in numbers only:
	$32.6
	" 36.4 " is not a valid input :( , please provide the hours worked in numbers

please provide your working hours in numbers only:
	36.4
please provide your current rate per hour in numbers only:
	$32.6
	" 36.4 " is not a valid input :( , please provide the hours worked in numbers

please provide your working hours in numbers only:
	36.4
please provide your current rate per hour in numbers only:
	$32.6
	calulating pay for 36.4 hours as per $ 32.6 per hour...
Traceback (most recent call last):
  File "/Users/pkewlani/Documents/py4e/textbook-ex3-1.py", line 28, in <module>
    print("hey! did you know you're just",40-hours_converted,"away from earning 1.5x your pay!\nput in a bit more in next time and take the jackpot!")
                                             ^^^^^^^^^^^^^^^
NameError: name 'hours_converted' is not defined. Did you mean: 'hours_convtd'?

please provide your working hours in numbers only:
	36.5
please provide your current rate per hour in numbers only:
	$32.9
calulating pay for 36.5 hours as per $ 32.9 per hour...
hey! did you know you're just 3.5 away from earning 1.5x your pay!
put in a bit more in next time and take the jackpot!
your current pay totals to $ 1200.85

please provide your working hours in numbers only:
	41.4
please provide your current rate per hour in numbers only:
	$32.9
whoa! you just unlocked 1.5x pay!! 
keep working 40+ hrs to keep up this momentum!
calulating pay for 41.4 hours as per $ 32.9 per hour...
your actual pay totals to: $ 1362.06 BUT
working 40+ hrs just earned you $ 2043.0899999999997 !

please provide your working hours in numbers only:
	28
please provide your current rate per hour in numbers only:
	$32.9
calulating pay for 28.0 hours as per $ 32.9 per hour...
your pay totals to $ 921.1999999999999

please provide your working hours in numbers only:
	45
please provide your current rate per hour in numbers only:
	$32.9
whoa! you just unlocked 1.5x pay!! 
keep working 40+ hrs to keep up this momentum!
calulating pay for 45.0 hours as per $ 32.9 / hour...
your actual pay totals to: $ 1480.5 BUT
working 40+ hrs just earned you $ 2220.75 !


"""