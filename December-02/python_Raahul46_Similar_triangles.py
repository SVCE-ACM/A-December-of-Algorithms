#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def check_tri(side1,side2,ang1,ang2):
    if((side1[0]/side2[0])==(side1[1]/side2[1])==(side1[2]/side2[2])):
        print("SIMILAR TRIANGLES,BY SSS")
    elif((side1[0]/side2[0])==(side1[1]/side2[1]) or
         (side1[1]/side2[1])==(side1[2]/side2[2]) or
         (side1[0]/side2[0])==(side1[2]/side2[2]))or (ang1[1]==ang2[1]):

        print("SIMILAR TRIANGLES,BY SAS")
    elif((ang1[0]==ang2[0]) or (ang1[0]==ang2[1]) or (ang1[0]==ang2[2]) or
         (ang1[1] == ang2[0]) or (ang1[1] == ang2[1]) or (ang1[1] == ang2[2])or
         (ang1[2] == ang2[0]) or (ang1[2] == ang2[1]) or (ang1[2] == ang2[2])):

        print("SIMILAR TRIANGLES,BY AA")



def main():
    side1=[]
    side2=[]
    side=0

    angle1=[]
    angle2=[]
    angle=0
    for i in range(0,3):
        side=int(input("ENTER {} SIDE FOR TRIANGLE1".format(i+1)))
        side1.append(side)

    for i in range(0, 3):
        side = int(input("ENTER {} SIDE FOR TRIANGLE2".format(i + 1)))
        side2.append(side)
    for i in range(0,3):
        angle=int(input("ENTER {} ANGLE FOR TRIANGLE1".format(i+1)))
        angle1.append(angle)
    for i in range(0,3):
        angle=int(input("ENTER {} ANGLE FOR TRIANGLE2".format(i+1)))
        angle2.append(angle)
    check_tri(side1,side2,angle1,angle2)
if __name__ == '__main__':
      main()
