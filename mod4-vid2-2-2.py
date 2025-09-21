try:
	eee='hello ' + "there's"
	eee=eee+1
except:
	print("the first one is a ",type(eee), "type, cannot be added to",type(1))

#output: the first one is a  <class 'str'> type, cannot be added to <class 'int'>