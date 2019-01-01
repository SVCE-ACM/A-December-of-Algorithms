import random

def binary_search( x, start, end):
	
		mid = int((start + end)/2)
		if(x>mid):
			print('Higher')
			binary_search(x,mid+1,end)
		elif (x<mid):
			print('Lower')
			binary_search(x,start,mid-1)
		else:
			print(mid,' is right. Your guess is spot on!')
			exit(0)
	
def main():
	player_a_choice = random.randint(0,100)
	print('Player B now starts guessing')
	binary_search(player_a_choice,0,100)
			
main()