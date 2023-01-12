number= int(input())
total_cost = (10 * 2000000) + 1000000
total_sale = number * 3000000

if(total_sale > total_cost):
	print("Profit")
	
elif(total_sale < total_cost):
	print("Loss")
	
else:
	print("Broke Even")
