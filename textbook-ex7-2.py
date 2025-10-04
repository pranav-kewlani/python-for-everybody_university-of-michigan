#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
#reading file name already implemented in ex7.1; importing logic to read file and relevant try-except logic



#attempting to use the lines from the code in above file here as well

#print(lines[10:26])	#test print succeeded but printed the first line instead of 12th | confirmed, code of interest in lines 11 through 27 | just learned that the lines from a file are stored as a list of strings when the readlines() method is used.
#could not figure out, googled and got to know that the above can be done using the import statement (to import entire fuctions from the file) or using the "from...import...." combo (to import only certain classes/functions from the file)

file_name_inp=input("enter file name to read through:\t")

from textbook_ex7_1 import read_inp_file
read_inp_file(file_name_inp)