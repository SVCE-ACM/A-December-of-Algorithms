def moveDisk(fp,tp):
    print(fp,"=>",tp)
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def Hanoi(n):
    moveTower(n,"left","right","middle")   
height=int(input('Enter the number of disks: '));
Hanoi(height)

