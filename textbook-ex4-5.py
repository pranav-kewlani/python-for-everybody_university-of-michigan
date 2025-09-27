#Exercise 5: What will the following Python program print out?

"""	expected output:
ABC
Zap
ABC

"""


def fred():
	print("Zap")
def jane():
	print("ABC")
jane()
fred()
jane()


#output:
#ABC
#Zap
#ABC
