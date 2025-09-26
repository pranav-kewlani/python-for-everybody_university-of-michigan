#Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.

repeat_lyrics()	#moving function call to the top to check error message

def print_lyrics():	#og function
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

def repeat_lyrics():	#function nesting
	print_lyrics()
	print_lyrics()


"""	output (error message):

Traceback (most recent call last):
  File "/Users/pkewlani/Documents/py4e/textbook-ex4-2.py", line 3, in <module>
    repeat_lyrics()	#moving function call to the top to check error message
    ^^^^^^^^^^^^^
NameError: name 'repeat_lyrics' is not defined	<- error message

"""