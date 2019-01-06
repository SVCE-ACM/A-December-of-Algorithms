#function to move disks
def TowerOfHanoi(n , from_rod, to_rod, mid_rod): 
    if n == 1: 
        print( "Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    #recursive call
    TowerOfHanoi(n-1, from_rod, mid_rod, to_rod) 
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod) 
    TowerOfHanoi(n-1, mid_rod, to_rod, from_rod) 
          
#getting no.of disks from the user 
n=int(input("Enter the number of disks:"))
#function call
TowerOfHanoi(n, 'A', 'C', 'B')  

  
