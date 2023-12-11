import random
r=random.randint(1,20)
while(True):
	inp=int(input())
	if(inp<r):
		print("wrong guess try greater number")
	elif(inp>r):
		print("wrong guess try smaller number")
	else:
		print("congrats,you ve guessed")
		break;    

		 s