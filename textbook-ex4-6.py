#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours_cal,rate_cal):
	if hours_cal>40:
		#just realised, calculating 1.5x the hrs here diaplays the wrong message
		print("Whoa! you worked",hours_cal,"hours this week!\nSince you surpassed the standard 40 working hrs/week, we'll assume you worked",hours_cal*1.5,"hours this week :)")
		hours_cal=hours_cal*1.5	#lets say working std hrs=40, overtime => 1.5x hours |
	elif 35<=hours_cal<=40:
		print("Hey you're quite close to the standard working hours.\nDid you know we consider 1.5x your hours if you surpass the standard 40 hours/week ?")
	
	total_cal=hours_cal*rate_cal
	return total_cal


#original logic:
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
		#modification starts here, simply calling the function will suffice instead of the entire calculation
		print("calculating your total pay for working",hours_convtd,"hours as per $",rate_convtd,"/hr rate...")
		payout=computepay(hours_convtd,rate_convtd)	#function call with hours & rate input as args | just realised the total_cal returned from the function was never stored and printed here 😅
		print("your total pay is: $",payout)
	else:
		print('"',rate,'"',"is not a valid input :( , please provide the rate in numbers")
else:
	print('"',hours,'"',"is not a valid input :( , please provide the hours worked in numbers")


"""	output:

please provide your working hours in numbers only:
	five
please provide your current rate per hour in numbers only:
	$20
" five " is not a valid input :( , please provide the hours worked in numbers

please provide your working hours in numbers only:
	41
please provide your current rate per hour in numbers only:
	$10.five
" 10.five " is not a valid input :( , please provide the rate in numbers

please provide your working hours in numbers only:
	40.5
please provide your current rate per hour in numbers only:
	$32.8
calculating your total pay for wokring 40.5 as per $ 32.8 /hr rate...
Whoa! you worked 60.75 hours this week!
Since you surpassed the standard 40 working hrs/week, we'll assume you worked 60.75 hours this week :)
#as indicated in line 35, did not store & print the value returned by the computepay function

please provide your working hours in numbers only:
	42
please provide your current rate per hour in numbers only:
	$32.8
calculating your total pay for wokring 42.0 hours as per $ 32.8 /hr rate...
Whoa! you worked 42.0 hours this week!
Since you surpassed the standard 40 working hrs/week, we'll assume you worked 63.0 hours this week :)
your total pay is: $ 2066.3999999999996

"""