def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print(fp," => ",tp)


disk=int(input("No of Disks: "))
print("Hanoi("+str(disk)+")")
moveTower(disk,"left","right","middle")
