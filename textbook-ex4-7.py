#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score_param):
	if 0<=score_param<=1:
		if 0.9<=score_param<=1.0:
			print("Grade A")
		elif 0.8<=score_param<=0.9:
			print("Grade B")
		elif 0.7<=score_param<=0.8:
			print("Grade C")
		elif 0.6<=score_param<=0.7:
			print("Grade D")
		else:
			print("Grade F")
	else:
		print("please provide a pupil score in the range 0.0 & 1.0 only")





#og logic:
score_inp=input("please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:\n")

try:
	score=float(score_inp)
	counter1=score
except:
	counter1=-1

if counter1>=0:
	#entire grade calculation logic shifted inside the funtion at line4
	computegrade(score)	#calling computegrade function with score (converted to float) as arg
else:
	print("Bad Input\n",'"',score_inp,'"',"is not a valid input, please provide the score in the range 0.0 & 1.0 in numbers only")


"""	output:
please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	0.95
Grade A

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

please provide pupil score between 0.0 & 1.0 (1.0 is 100% score) in numbers only:
	.5
Grade F

"""