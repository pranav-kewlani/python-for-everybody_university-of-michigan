#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and
#then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

#Expected output:
#Enter the file name: mbox-short.txt
#Average spam confidence: 0.750718518519




#logic for reading file name and handling the file already implemented in ex7.1; importing logic to read file and relevant try-except logic

#attempting to use the lines from the code in above file here as well

#print(lines[10:26])	#test print succeeded but printed the first line instead of 12th | confirmed, code of interest in lines 11 through 27 | just learned that the lines from a file are stored as a list of strings when the readlines() method is used.
#could not figure out, googled and got to know that the above can be done using the import statement (to import entire fuctions from the file) or using the "from...import...." combo (to import only certain classes/functions from the file)

#tried several methods, but from what i understood after looking up on google & chatgpt, even though only the specfic function to process the file name from user input gets imported from ex7.1 file, the entire file is run (or interpreted before ex7.2 file)
#hence 'not defined' errors for a couple local variables
#came across a couple other methods on chatgpt/googleAI, but some seemed pretty complex and others didnt work
#implementing the logic manually now

user_inp_file_name=input("provide name of the file from which lines are to be scanned:\t")

try:
	fhand_read=open(user_inp_file_name)
	lines=fhand_read.readlines()
	check1="success"
except:
	print("file with name",'"',user_inp_file_name,'"',"not found")
	try_again=input("do you want to try again? Y/N\t")
	if try_again.upper()=="Y":
		user_inp_file_name=input("provide name of the file from which lines are to be scanned:\t")
		check1="success"
	else:
		exit("Thanks :)\nYou either could not provide a valid file name or chose to exit")

if check1=="success":
	spam_conf_total=0
	spam_conf_count=0
	for current_line in lines:
		current_line=current_line.rstrip()
		
		if current_line.startswith("X-DSPAM-Confidence")==False: continue
		
		else:
			colon_pos=current_line.find(":")
			sp_pos=current_line.find(" ",colon_pos)
			current_line_spam_conf_value=current_line[sp_pos+1:]
			spam_conf_count+=1
			spam_conf_total+=float(current_line_spam_conf_value)

	print("the total spam confidence value across this file is ",spam_conf_total,", averaging to ",spam_conf_total/spam_conf_count,"across",spam_conf_count,"values")


"""	output:
provide name of the file from which lines are to be scanned:	practice resources/mbox-short.txt
the total spam confidence value across this file is  20.269400000000005 , averaging to  0.7507185185185187 across 27 values

"""