#Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?


def repeat_lyrics():	#function nesting
	print_lyrics()
	print_lyrics()

	def print_lyrics():	#moving this to be defined after the repeat_lyrics() funcn (in which the print_lyrics() is called); assumption - should generate the same error, "print_lyrics is not defined"
		print("I'm a lumberjack, and I'm okay.")
		print('I sleep all night and I work all day.')

repeat_lyrics()	#moving function call to bottom again


"""	output (error message):

Traceback (most recent call last):
  File "/Users/pkewlani/Documents/py4e/textbook-ex4-3.py", line 12, in <module>
    repeat_lyrics()	#moving function call to bottom again
    ~~~~~~~~~~~~~^^
  File "/Users/pkewlani/Documents/py4e/textbook-ex4-3.py", line 5, in repeat_lyrics
    print_lyrics()
    ^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'print_lyrics' where it is not associated with a value


"""