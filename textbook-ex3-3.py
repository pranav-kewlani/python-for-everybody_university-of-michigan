#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
#	Score Grade:
#	>= 0.9 A check
#	>= 0.8 B check
#	>= 0.7 C check
#	>= 0.6 D check
#	< 0.6 F check

#	test cases:
#	0.95 -> A check
#	perfect ->	Bad score check
#	10.0 ->	Bad score check
#	0.75 ->	C check
#	0.5 ->	F check

score_inp=input("please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:\n")

try:
	score=float(score_inp)
	counter1=score
except:
	counter1=-1

if counter1>=0 and 0<=score<=1:
	if 0.9<=score<=1.0:
		print("Grade A")
	elif 0.8<=score<=0.9:
		print("Grade B")
	elif 0.7<=score<=0.8:
		print("Grade C")
	elif 0.6<=score<=0.7:
		print("Grade D")
	else:
		print("Grade F")
elif counter1>=0 and (score<0 or score>1):	#wrong variable name for counter
	print("please provide a pupil score in the range 0.0 & 1.0 only")
else:
	print("Bad Input\n",'"',score_inp,'"',"is not a valid input, please provide the score in the range 0.0 & 1.0 in numbers only")


"""	output:
pkewlani@Pranavs-MacBook-Air py4e % python3 textbook-ex3-3.py                                                         
please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	0.95 
Grade A

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	0.8
Grade B

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	0.7
Grade C

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	0.6
Grade D

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	0.5
Grade F

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	perfect
Traceback (most recent call last):
  File "/Users/pkewlani/Documents/py4e/textbook-ex3-3.py", line 35, in <module>
    elif counter>=0 and (score<0 or score>1):
         ^^^^^^^
NameError: name 'counter' is not defined. Did you mean: 'counter1'?

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	perfect
Bad Input
 " perfect " is not a valid input, please provide the score in the range 0.0 & 1.0 in numbers only

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
10  
please provide a pupil score in the range 0.0 & 1.0 only

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	0.75
Grade C

"""