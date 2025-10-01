#Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
#python shout.py
#Enter a file name: mbox-short.txt
#FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
#RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#SAT, 05 JAN 2008 09:14:16 -0500
#file downloaded from www.py4e.com/code3/mbox-short.txt

file_name_inp=input("enter file path including name:\n")

try:
	fhand_read=open(file_name_inp)
	check1="success"
except:	
	print("file with name",'"',file_name_inp,'"',"not found")
	try_again=input("do you wish to try again? y/n\t")	#if user wants to try again, re-request file name
	if try_again.upper()=="Y":	#forgot to put Y in double quotes here
		file_name_inp=input("enter file path including name:\n")
		check1="success"
	else:	#if no, exit execution
		print("alright\nthanks")
		exit()	#used break here by mistake, faced error "break outside loop" continuously

if check1=="success":	
	try:
		num_of_lines_inp=input("enter the number of lines to be printed from the file (integers only): ")	#collect and convert number of lines to be printed to int only if file successfully located
		inp_lines_conv=int(num_of_lines_inp)
		check2="success"
	except:
		check2="failure"
		
		retry_counter=5
		while retry_counter>0:	#allow the user try only 5 more times
			print('"',num_of_lines_inp,'"',"is not a valid input")

			try_again=input("do you wish to try again? y/n\t")	#if user wants to try again, re-request file name
			if try_again.upper()=="Y":	#forgot to put Y in double quotes here

				print("you have",retry_counter,"attempts left")
				retry_counter-=1	#originally wrote this as "retry_counter=-1", which assigned -1 to the var instead of decrementing it by 1. execution jumped to the line59 and traceback at line60
				num_of_lines_inp=input("enter the number of lines to be printed from the file (integers only): ")	#retry to collect the num of lines to be printed
				try:
					inp_lines_conv=int(num_of_lines_inp)
					check2="success"
					break
				except:
					check2="failure"
					continue

			else:	#if no, exit execution
				print("alright\nthanks\n no valid int input or you chose to quit")
				exit()


if check2=="success":	#did not implement this before, faced error as execution jumped to line59 despite five invalid entries for number of lines to be read from file
	lines=fhand_read.readlines()
	for i,line in enumerate(lines):	#came across the enumerate function to index the items in a for loop obj as well; i used as the indexer
		if i<int(num_of_lines_inp):
			line=line.upper().rstrip()
			print(line)
else:
	print("you failed to provide valid input for the number of lines to be read from the file",'"',file_name_inp,'"')

""" output
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
	 BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
	 SAT, 05 JAN 2008 09:14:16 -0500
X-SIEVE: CMU SIEVE 2.3
------------------------------------------------------------

run-1: invalid file name & chose not to try again
enter file path including name:
practice resou
file with name " practice resou " not found
do you wish to try again? y/nn
alright
thanks
------------------------------------------------------------

run-2: invalid line count & chose not to cont
enter file path including name:
practice resources/mbox-short.txt
enter the number of lines to be printed from the file (integers only): six
" six " is not a valid input
do you wish to try again? y/n	n
alright
thanks
 you either no valid int input or you chose to quit
------------------------------------------------------------

run-3: invalid line count & choose to cont
enter file path including name:
practice resources/mbox-short.txt
enter the number of lines to be printed from the file (integers only): seven
" seven " is not a valid input
do you wish to try again? y/n	y
you have 5 attempts left
enter the number of lines to be printed from the file (integers only): six
" six " is not a valid input
do you wish to try again? y/n	y
you have 4 attempts left
enter the number of lines to be printed from the file (integers only): five
" five " is not a valid input
do you wish to try again? y/n	y
you have 3 attempts left
enter the number of lines to be printed from the file (integers only): four
" four " is not a valid input
do you wish to try again? y/n	y
you have 2 attempts left
enter the number of lines to be printed from the file (integers only): three
" three " is not a valid input
do you wish to try again? y/n	y
you have 1 attempts left
enter the number of lines to be printed from the file (integers only): two
you failed to provide valid input for the number of lines to be read from the file " practice resources/mbox-short.txt "

------------------------------------------------------------

run-4: valid file & valid line number count:
enter file path including name:
practice resources/mbox-short.txt
enter the number of lines to be printed from the file (integers only): six
" six " is not a valid input
do you wish to try again? y/n	y
you have 5 attempts left
enter the number of lines to be printed from the file (integers only): 4
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
	 BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;

"""