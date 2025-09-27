#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(str_arg,letter_arg):
	count=0
	for lett in strS:
		if lett==letter_arg:
			count=count+1
	return count

strS=input("provide a string:\n")
inp_lett=input("what letter's frequency do you need? ")
print("the letter",'"',inp_lett,'"',"is present",count(strS,inp_lett),"times in the string",'"',strS,'"') #trying to get the indices at which the letters occur as well; could not, maybe while loop would help. but objects will surely make easier.


"""	output:
provide a string:
pranav
what letter's frequency do you need? a
the letter " a " is present 2 times in the string " pranav "

"""