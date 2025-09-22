# second experience with a try-except block,
# learning: the entire code/logic should never be put inside a try-except block, results in even the healthy parts of the code not being executed.
# only put the doubtful part of the code in try-except

strA= "Bob"
try:
	print("Hello there")
	strI= int(strA)
	print("How are you") #this should have been executed, does not contain any errors. But will not be executed, bec the exeution will jump to the except block due to the Traceback at line 8

except:
	strI=-1

print ("end of code, I =", strI)

