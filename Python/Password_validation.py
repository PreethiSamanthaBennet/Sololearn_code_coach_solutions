x = input()
y = ['!','@','#','$','%','&','*']
z = ['0','1','2','3','4','5','6','7','8','9']
a = 0
b = 0

for i in x:

	if i in z:
		a = a + 1
	
	elif i in y:
		b = b + 1
	
	
if (len(x) >=7) and (a>=2)and (b>=2):
	print("Strong")
	
else:
	print("Weak")
