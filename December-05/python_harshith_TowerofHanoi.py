def moveTower(height,frompole, topole, withpole):
    if height >= 1:
        moveTower(height-1,frompole,withpole,topole)
        moveDisk(frompole,topole)
        moveTower(height-1,withpole,topole,frompole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
a=int(input("Enter the number of disks"))
moveTower(a,"A","B","C")
