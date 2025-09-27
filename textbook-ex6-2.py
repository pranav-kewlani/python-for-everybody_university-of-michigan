#Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# predicted answer: will return "banana" (entire string) bec skipping first index will return from first index and skipping the last one will return until the last index
# had a second thought that this might return an empty string as both values are equal, but turns out python considers values as euqal only when there actually are values.

fruit="banana"
print(fruit[:])

"""	output:
banana

"""