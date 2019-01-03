# Dec 2
def AAA(a1, a2):
    if a1 == a2:
        return True
    return False


def SAS(s1, s2, a1, a2):
    if (s1[0] / s2[0]) == (s1[1] / s2[1]):
        if a1[2] == a2[2]:
            return True

    if (s1[1] / s2[1]) == (s1[2] / s2[2]):
        if a1[0] == a2[0]:
            return True

    if (s1[2] / s2[2]) == (s1[0] / s2[0]):
        if a1[1] == a2[1]:
            return True

    return False


def SSS(s1, s2):
    if (s1[0] / s2[0] == s1[1] / s2[1]) and (s1[1] / s2[1] == s1[2] / s2[2]) and (s1[2] / s2[2] == s1[0] / s2[0]):
        return True
    return False


# Enter numbers with spaces not commas!
s1 = list(map(float, input("Enter the sides for triangle 1: ").split()))
a1 = list(map(float, input("Enter the angles for triangle 1: ").split()))
s2 = list(map(float, input("Enter the sides for triangle 2: ").split()))
a2 = list(map(float, input("Enter the angles for triangle 2: ").split()))
s1.sort()
s2.sort()
a1.sort()
a2.sort()
aaa = AAA(a1, a2)
sas = SAS(s1, s2, a1, a2)
sss = SSS(s1, s2)
if aaa or sss or sas:
    print("Triangles are similar by", end=" ")
    if aaa:
        print("AAA", end=" ")
    if sss:
        print("SSS", end=" ")
    if sas:
        print("SAS", end=" ")
else:
    print("Triangles are not similar")

# SAMPLE I/O
# Enter the sides for triangle 1: 2 3 3
# Enter the angles for triangle 1: 80 60 40
# Enter the sides for triangle 2: 4 6 6
# Enter the angles for triangle 2: 40 60 80
# Triangles are similar by AAA SSS SAS
