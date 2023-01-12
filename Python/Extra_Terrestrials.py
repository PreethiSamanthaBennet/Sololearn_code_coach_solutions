def reverse(string):
    reversed = ""
    for i in string:
        reversed  = i+reversed
    print(reversed) 

string = input()

reverse(string)
