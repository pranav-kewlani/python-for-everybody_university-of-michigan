# Exercise 5: Slicing strings Take the following Python code that stores a string: str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

strS="X-DSPAM-Confidence: 0.8475"
col_pos=strS.find(":")
print(": is at index",col_pos)

spc_pos=strS.find(" ",col_pos)
print("the space after colon is at index",spc_pos)

tgt_value=strS[spc_pos+1:]

print("target value =",float(tgt_value))
print("adding 1 to proove target value: ",float(tgt_value)+1)


"""	output:
: is at index 18
the space after colon is at index 19
target value = 0.8475
adding 1 to proove target value:  1.8475000000000001

"""