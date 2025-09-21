xx=1
print("xx is of type:",type(xx))

temp=98.0
print("temp is of type:",type(temp))

"""   output:
xx is of type: <class 'int'>
temp is of type: <class 'float'>   """

#dividing int by 100 to understand division in python 3
div=1/100
print("result:",div,"; type=",type(div))

#output: result: 0.01 ; type= <class 'float'>


#example of converting int to float and adding to another constof type integer:
print(type(xx),xx,"converted to",type(float(xx)),"and added to 100 gives",float(xx)+100,", which is of type",type(float(xx)+100))

"""   output:
<class 'int'> 1 converted to <class 'float'> and added to 100 gives 101.0 , which is of type <class 'float'>   """