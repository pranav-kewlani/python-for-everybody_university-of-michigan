#Exercise 6: use strip and replace methods in a program

fruit=" b anana   "

print("stripped bar from banana: ",fruit.strip("bar"))	#should result in "nana"
print("strip in banana with no args:",fruit.strip())	#should result in "b anana"

print("simple replace in banana",fruit.replace("b","sh"))	#should result in shanana; 
print("count replace in banana",fruit.replace("na","naa",count=1))	#should result in banaana; 

"""	output:
stripped bar from banana:   b anana   (not stripping because "b " found in "b anana" but "ba" not found)
strip in banana with no args: b anana  (correct; confirmed, simple stripping does not replace spaces between chars)
simple replace in banana  sh anana   (missed on the space between "b" & "anana")
count replace in banana  b anaana 	(missed on the space between "b" & "anana")

"""