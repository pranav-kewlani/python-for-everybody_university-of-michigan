# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

strS=input("provide a single word:\n")

index=-1
while index>= (-1*len(strS)):
	print(index,"th letter in",strS,"is:   ",strS[index])
	index-=1

"""	output:
provide a single word:
banana
-1 th letter in banana is:    a
-2 th letter in banana is:    n
-3 th letter in banana is:    a
-4 th letter in banana is:    n
-5 th letter in banana is:    a
-6 th letter in banana is:    b

"""
