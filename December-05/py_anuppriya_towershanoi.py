def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    
    print(fp,"=>",tp)

print("TOWERS OF HANOI")
n=int(input("Enter the number of disks: "))
print("Moving disk from: ")

moveTower(n,"Left","Right","Middle")





