string = input()

char=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')

for i in string:
	if i not in char:
		string = string.replace(i,'')
		

def reverse(string):
	reversed= ""
	for i in string:
		reversed = i+reversed
	print(reversed)
	
reverse(string)
