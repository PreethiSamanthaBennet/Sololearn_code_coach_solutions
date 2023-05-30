list = []

n = int(input())

for i in range(n):
   list.append(int(input()))
   
sum = sum1 = 0
count = 0
for i in range(n):
	if list[i] % 2 == 0:
		sum += list[i]
		count += 1
		
	if list[i] % 2 != 0:
		sum1 += list[i]
		count += 1
		
print(sum)
