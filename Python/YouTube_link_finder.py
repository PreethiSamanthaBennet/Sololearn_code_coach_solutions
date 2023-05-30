link = input()

if 'https://www.youtube.com/watch?v=' in link:
	link = link.replace('https://www.youtube.com/watch?v=','')
	
if 'https://youtu.be/' in link:
	link = link.replace('https://youtu.be/','')
print(link)
