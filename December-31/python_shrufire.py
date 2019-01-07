def Distance(start, point, length):
    return min((start[0]-point[0])%length,(point[0]-start[0])%length) + min((start[1]-point[1])%length,(point[1]-start[1])%length) 

def ClosestEnemyII(strArr): 
    start = []
    for i in range(0,len(strArr)):
        if "1" in strArr[i]:
            start = [i, strArr[i].find("1")]
    if start == []:
        return 0
    answer = 2*len(strArr)
    for i in range(0,len(strArr)):
        for j in range(0,len(strArr)):
            if strArr[i][j]=="2":
                if Distance(start, [i,j], len(strArr)) < answer:
                    answer = Distance(start, [i,j], len(strArr))
    return answer
s=input('Enter the elements row-wise: ')
print(ClosestEnemyII(s.split(',')))  

