#Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than a integers, detect their mistake
#using try and except and print an error message and skip to the next integers.
#	Enter a number: 4
#	Enter a number: 5
#	Enter a number: bad data
#	Invalid input
#	Enter a number: 7
#	Enter a number: done
#	16 3 5.333333333333333

print("Welcome to the program that accepts integers and then provides: \n1. the total number of inputs\n2. valid inputs \n3. invalid inputs \n4. sum of all valid inputs\n5. average of all valid inputs\n")
print("===NOTE===\n->only integers are accepted as valid inputs\n->type 'done' at any time to end the inputs and display the end results\n")

#defining a function that performs the sum of its args
def sum_fun(a,b):
	sum=a+b
	return sum

#defining a function that puts out the average its args
def avg_fun(total,avg_count):
	avg=total/avg_count
	return avg

#using while loop as we want the iteration to run indefinitely until the user's prompt "done"

index=0	#init total count var
valid_inp_count=0	#init the valid input count var
invalid_inp_count=0	#init the invalid input count var
inp_total=0 #init the input total var
inp_avg=0 #init the input avg var

while True:
	user_inp=input("provide the next int or put in 'done' to end input: ")
	#if user_inp=="done":
		#break	originally added the break statement against "done input by the user here but then realised that the end results need to be displayed as well, so added an elif block at line48
	try:
		conv_inp=int(user_inp)	#try converting user input to int
		check1=conv_inp
	except:
		#check1=6.18034		originally put 6.18034 as the check value thinking that its a float value and would not be accepted as input by the user, bu then realised that the int() funcn does convert float values to int by simply chopping off the fraction part
		check1="invalid"	#new check value
	
	if check1!="invalid":  #increment valid inp count and display progressive results for each input
		index=index+1
		valid_inp_count=valid_inp_count+1
		print("your input at index",index,"is: ",conv_inp)
		inp_total=sum_fun(inp_total,conv_inp)
		inp_avg=avg_fun(inp_total,valid_inp_count)
		print("the total of",valid_inp_count,"valid inputs so far is",inp_total,"and their average is",inp_avg,"\n")
	
	elif check1=="invalid" and user_inp=="done":  #added this block realising that if the check value becomes invalid even if the user provides "done" as input, which is a valid input. thus if check is set to invalid due to this reason, display the end result. added this block between the if & else blocks as only the first correct block gets executed in an if-elif-else combo. if this logic was put into else block starting at line54, the loop would keep continuing and the end result would never be triggered even if the user put in "done".
		print("Alright! nice working with",index,"inputs! Here are the end results:\n")
		print("1. Total Inputs: ",index,"\n2. Valid Inputs: ",valid_inp_count,"\n3. Invalid Inputs: ",invalid_inp_count,"\n4. TOTAL of all valid inputs:",inp_total,"\n5. AVERAGE of all valid inputs:",inp_avg)
		print("Please note,",int(valid_inp_count/index*100),"% of your inputs were valid and",int(invalid_inp_count/index*100),"% of your inputs were invalid")		#added int() finction to percentage calculation here
		break
	
	else:	#if completely invalid input, display error message & continue to the top of the loop
		index=index+1	#forgot to increment index here
		invalid_inp_count=invalid_inp_count+1	#put '+' instead of '=' here, resulted into miscalculated invalid input count
		print('"',user_inp,'"',"is not a valid input, please provide a number\n") #just realised, the input count is never incremented for invalid inputs. segregating and adding representation of valid vs invalid inputs & total inputs
		continue


"""	output:
RUN-1:
Welcome to the program that accepts integers and then provides: 
1. the number of integers put in
2. sum of all integers
3. average of the integers

===NOTE===
->only integers are accepted as valid inputs
->type 'done' at any time to end the inputs and display the end results

provide the next int or put in 'done' to end input: 12
your input at index 1 is:  12
the total of 1 inputs so far is 12 and their average is 12.0 

provide the next int or put in 'done' to end input: 12
your input at index 2 is:  12
the total of 2 inputs so far is 24 and their average is 12.0 

provide the next int or put in 'done' to end input: 12
your input at index 3 is:  12
the total of 3 inputs so far is 36 and their average is 12.0 

provide the next int or put in 'done' to end input: (i pressed enter mistakenly without an input)
"  " is not a valid input, please provide a number

provide the next int or put in 'done' to end input: 0
your input at index 4 is:  0
the total of 4 inputs so far is 36 and their average is 9.0 

provide the next int or put in 'done' to end input: 56
your input at index 5 is:  56
the total of 5 inputs so far is 92 and their average is 18.4 

provide the next int or put in 'done' to end input: thirty five
" thirty five " is not a valid input, please provide a number

provide the next int or put in 'done' to end input: 35
your input at index 6 is:  35
the total of 6 inputs so far is 127 and their average is 21.166666666666668 

provide the next int or put in 'done' to end input: 49
your input at index 7 is:  49
the total of 7 inputs so far is 176 and their average is 25.142857142857142 

provide the next int or put in 'done' to end input: 90
your input at index 8 is:  90
the total of 8 inputs so far is 266 and their average is 33.25 

provide the next int or put in 'done' to end input: done
Alright! nice working with 8 numbers! Here are the end results:

1. Number of inputs:  8 
2. TOTAL: 266 
3. AVERAGE: 33.25

-----------------------------------------------------------------
FINAL RUN:
Welcome to the program that accepts integers and then provides: 
1. the total number of inputs
2. valid inputs 
3. invalid inputs 
4. sum of all valid inputs
5. average of all valid inputs

===NOTE===
->only integers are accepted as valid inputs
->type 'done' at any time to end the inputs and display the end results

provide the next int or put in 'done' to end input: 4
your input at index 1 is:  4
the total of 1 valid inputs so far is 4 and their average is 4.0 

provide the next int or put in 'done' to end input: 5
your input at index 2 is:  5
the total of 2 valid inputs so far is 9 and their average is 4.5 

provide the next int or put in 'done' to end input: bad data
" bad data " is not a valid input, please provide a number

provide the next int or put in 'done' to end input: 7
your input at index 4 is:  7
the total of 3 valid inputs so far is 16 and their average is 5.333333333333333 

provide the next int or put in 'done' to end input: done
Alright! nice working with 4 inputs! Here are the end results:

1. Total Inputs:  4 
2. Valid Inputs:  3 
3. Invalid Inputs:  1 
4. TOTAL of all valid inputs: 16 
5. AVERAGE of all valid inputs: 5.333333333333333
Please note, 75.0 % of your inputs were valid and 25.0 % of your inputs were invalid

"""