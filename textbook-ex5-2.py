#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

#og logic:
print("\nWelcome to the program that accepts integers and then provides: \n1. the total number of inputs\n2. valid inputs \n3. invalid inputs \n4. sum of all valid inputs\n5. max from all valid inputs\n6. min from all valid inputs\n")
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

max_inp=None	#init the max var
max_inp_index=0	#to display which input was max
min_inp=None	#init the min var; error with init as 0, input 5 then 4, but did not store 4 as min input
min_inp_index=0	#to display which input was min


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
		if index==1:	#added this block considering if there's only one input from the user like at line123; realised this block should be here instead of at line50; put it at line45 but then realised it this input would never be added to the total if the excutions was directed to the top from here itself
			print(conv_inp,"is the only input so far")
			max_inp=min_inp=conv_inp #input 5 then 4, stil got 4 as both max and min inputs, so added this and line50
			max_inp_index=min_inp_index=index
			continue	#added, realised this was needed
		else:
			print("the total of",valid_inp_count,"valid inputs so far is",inp_total,"and their average is",inp_avg,"\n")
		
		if max_inp==None or conv_inp>max_inp:	#check and store if new entry is largest so far; realised this becomes if instead of elif now after changes at line47
			max_inp=conv_inp
			print(conv_inp,"is the largest input so far\n")
			max_inp_index=index
		if min_inp==None or conv_inp<min_inp:	#forgot to change the logic here after pasting from above, error occurred; realised this becomes if instead of elif now after changes at line47
			min_inp=conv_inp
			print(conv_inp,"is the smallest input so far\n")
			min_inp_index=index
	
	elif check1=="invalid" and user_inp=="done":  #added this block realising that if the check value becomes invalid even if the user provides "done" as input, which is a valid input. thus if check is set to invalid due to this reason, display the end result. added this block between the if & else blocks as only the first correct block gets executed in an if-elif-else combo. if this logic was put into else block starting at line54, the loop would keep continuing and the end result would never be triggered even if the user put in "done".
		if index==1:	#added this block extending logic at line48
			print("\nThere was only one input from your end :(")
			print("Thus, Total = Max = Min = Average =",conv_inp,"\n")
			break
		else:	#missed on indenting the block in lines65-68 after adding them into the else condition
			print("Alright! nice working with",index,"inputs! Here are the end results:\n")
			print("1. Total Inputs: ",index,"\n2. Valid Inputs: ",valid_inp_count,"\n3. Invalid Inputs: ",invalid_inp_count,"\n4. TOTAL of all valid inputs:",inp_total,"\n5. Max of all valid inputs:",max_inp,"(",max_inp_index,"th) input\n6. Min of all valid inputs:",min_inp,"(",min_inp_index,"th) input\n")	#used wrong variable names for max and min values
			print("Please note,",valid_inp_count/index*100,"% of your inputs were valid and",invalid_inp_count/index*100,"% of your inputs were invalid\n")		#added int() finction to percentage calculation here
			break
	
	else:	#if completely invalid input, display error message & continue to the top of the loop
		index=index+1	#forgot to increment index here
		invalid_inp_count=invalid_inp_count+1	#put '+' instead of '=' here, resulted into miscalculated invalid input count
		print('"',user_inp,'"',"is not a valid input, please provide a number\n") #just realised, the input count is never incremented for invalid inputs. segregating and adding representation of valid vs invalid inputs & total inputs
		continue


"""	output:
RUN-1:
Welcome to the program that accepts integers and then provides: 
1. the total number of inputs
2. valid inputs 
3. invalid inputs 
4. sum of all valid inputs
5. max from all valid inputs
6. min from all valid inputs

===NOTE===
->only integers are accepted as valid inputs
->type 'done' at any time to end the inputs and display the end results

provide the next int or put in 'done' to end input: 4
your input at index 1 is:  4
the total of 1 valid inputs so far is 4 and their average is 4.0 

4 is the largest input so far
provide the next int or put in 'done' to end input: 5
your input at index 2 is:  5
the total of 2 valid inputs so far is 9 and their average is 4.5 

5 is the largest input so far
provide the next int or put in 'done' to end input: -1
your input at index 3 is:  -1
the total of 3 valid inputs so far is 8 and their average is 2.6666666666666665 

-1 is the smallest input so far
provide the next int or put in 'done' to end input: 7
your input at index 4 is:  7
the total of 4 valid inputs so far is 15 and their average is 3.75 

7 is the largest input so far
provide the next int or put in 'done' to end input: 6
your input at index 5 is:  6
the total of 5 valid inputs so far is 21 and their average is 4.2 

6 is the smallest input so far
provide the next int or put in 'done' to end input: done
Alright! nice working with 5 inputs! Here are the end results:

Traceback (most recent call last):
  File "/Users/pkewlani/Documents/py4e/textbook-ex5-2.py", line 59, in <module>
    print("1. Total Inputs: ",index,"\n2. Valid Inputs: ",valid_inp_count,"\n3. Invalid Inputs: ",invalid_inp_count,"\n4. TOTAL of all valid inputs:",inp_total,"\n5. Max of all valid inputs:",inp_max,"(",max_inp_index,"th) input\n6. Min of all valid inputs:",inp_min,"(",min_inp_index,"th) input\n")
                                                                                                                                                                                                ^^^^^^^
NameError: name 'inp_max' is not defined


-------------------------------------------------------------------
RUN-2:
provide the next int or put in 'done' to end input: 5
your input at index 1 is:  5
the total of 1 valid inputs so far is 5 and their average is 5.0 

5 is the largest input so far

5 is the smallest input so far

provide the next int or put in 'done' to end input: done
Alright! nice working with 1 inputs! Here are the end results:

1. Total Inputs:  1 
2. Valid Inputs:  1 
3. Invalid Inputs:  0 
4. TOTAL of all valid inputs: 5 
5. Max of all valid inputs: 5 ( 1 th) input
6. Min of all valid inputs: 5 ( 1 th) input

Please note, 100 % of your inputs were valid and 0 % of your inputs were invalid

------------------------------------------------------------------
RUN-3:
Welcome to the program that accepts integers and then provides: 
1. the total number of inputs
2. valid inputs 
3. invalid inputs 
4. sum of all valid inputs
5. max from all valid inputs
6. min from all valid inputs

===NOTE===
->only integers are accepted as valid inputs
->type 'done' at any time to end the inputs and display the end results

provide the next int or put in 'done' to end input: 5
your input at index 1 is:  5
5 is the only input so far
provide the next int or put in 'done' to end input: 4
your input at index 2 is:  4
the total of 2 valid inputs so far is 9 and their average is 4.5 

4 is the smallest input so far

provide the next int or put in 'done' to end input: -1
your input at index 3 is:  -1
the total of 3 valid inputs so far is 8 and their average is 2.6666666666666665 

-1 is the smallest input so far

provide the next int or put in 'done' to end input: five
" five " is not a valid input, please provide a number

provide the next int or put in 'done' to end input: 45
your input at index 5 is:  45
the total of 4 valid inputs so far is 53 and their average is 13.25 

45 is the largest input so far

provide the next int or put in 'done' to end input: 7
your input at index 6 is:  7
the total of 5 valid inputs so far is 60 and their average is 12.0 

provide the next int or put in 'done' to end input: done
Alright! nice working with 6 inputs! Here are the end results:

1. Total Inputs:  6 
2. Valid Inputs:  5 
3. Invalid Inputs:  1 
4. TOTAL of all valid inputs: 60 
5. Max of all valid inputs: 45 ( 5 th) input
6. Min of all valid inputs: -1 ( 3 th) input

Please note, 83.33333333333334 % of your inputs were valid and 16.666666666666664 % of your inputs were invalid

------------------------------------------------------------------
RUN-4:
Welcome to the program that accepts integers and then provides: 
1. the total number of inputs
2. valid inputs 
3. invalid inputs 
4. sum of all valid inputs
5. max from all valid inputs
6. min from all valid inputs

===NOTE===
->only integers are accepted as valid inputs
->type 'done' at any time to end the inputs and display the end results

provide the next int or put in 'done' to end input: 4
your input at index 1 is:  4
4 is the only input so far
provide the next int or put in 'done' to end input: done
There was only one input from your end :(
Thus, Total = Max = Min = 4 


"""
