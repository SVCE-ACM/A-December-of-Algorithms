no_of_cr = int(input("Number of classrooms: "))
size = int(input("Size of classrooms (1-50): "))
depts = int(input("Enter the number of departments: "))
codes = []
for i in range(depts):
    print("Department",i+1,"code :",end='')
    code=input()
    codes.append([code, 0])
for i in range(depts):
    print("Students in department :",i+1,end='')
    codes[i][1] = int(input())
co = codes.copy()
c = 1
final = []
sub = []
i = 0
for x in range(no_of_cr):
    s = size
    while s > 0:
        if co[i][1]:
            sub.append(co[i][0]+str(c))
            co[i][1] -= 1
        else:
            sub.append('___')
        i += 1
        if len(sub) == 4:
            final.append(sub.copy())
            sub.clear()
        if i == len(co):
            c += 1
            i = 0
        s -= 1
f = final.copy()
for i in range(1, len(f), 2):
    f[i] = f[i][::-1]

f = [j for i in f for j in i]

c = 1
i = 0

while c <= no_of_cr:
    print("Room",c)
    j = 1
    for word in f[i:i+size]:
        if j > 4:
            print()
            j = 1
        print(word, end="\t")
        j += 1
    i += size
    c += 1
    print()
