import math
houses = int(input())

dollar_bill = (2*100)/houses

if(200 % houses == 0):
	print(int(dollar_bill))
	
else:
	print(math.ceil(dollar_bill))
