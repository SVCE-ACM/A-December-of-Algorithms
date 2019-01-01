def TowerOfHanoi(n , fro, to, mid): 
    if n == 1: 
        print (
		"Move disk 1 from rod",fro,"to rod",to) 
        return
    TowerOfHanoi(n-1, fro, mid, to) 
    print ("Move disk",n,"from rod",fro,"to rod",to) 
    TowerOfHanoi(n-1, mid, to, fro) 
          
n = int(input('Enter order'))
TowerOfHanoi(n, 'A', 'C', 'B')
