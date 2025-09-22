#experiencing deliberate try&except logic for the first time

#first logic, aimed to execute except block

strA= "Hello Bob"

try:
	strI= int(strA)	#this is erroneous as strings cannot be converted to ints
except:
	strI= -1

print("First try/except attempt = ",strI)

#second logic, aimed to execute try block

strA= "123"

try:
	strI= int(strA)
except:
	strI= -1

print("Second try/except attempt = ", strI)


""" output:
First try/except attempt =  -1
Second try/except attempt =  123
"""