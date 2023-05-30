string = input()

string = string.replace('x', '')

if 'G$T' in string:
	print("ALARM")

elif 'T$G' in string:
	print("ALARM")
	
else:
	print("quiet")
