# Dec 23
import numpy as np
num_of_classrooms = int(input("Number of classrooms "))
size = int(input("Size of classrooms (1-50) "))
depts = int(input("Enter the number of departments "))
codes = []
for i in range(depts):
    code = input(f"Department {i+1} code ")
    codes.append([code, 0])
for i in range(depts):
    num = int(input(f"Students in department {i+1} (1-100) "))
    codes[i][1] = num
co = codes.copy()
c = 1
final = []
sub = []
i = 0
for x in range(num_of_classrooms):
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
new_f = list(np.array(f).flatten())


c = 1
i = 0

while c <= num_of_classrooms:
    print(f"Room {c}")
    j = 1
    for word in new_f[i:i+size]:
        if j > 4:
            print()
            j = 1
        print(word, end="\t")
        j += 1
    i += size
    c += 1
    print()

# Sample I/O
# Number of classrooms 2
# Size of classrooms (1-50) 16
# Enter the number of departments 2
# Department 1 code CS
# Department 2 code EC
#
# Students in department 1 (1-100) 15
# Students in department 2 (1-100) 16
# Room 1
# CS1     EC1     CS2     EC2
# EC4     CS4     EC3     CS3
# CS5     EC5     CS6     EC6
# EC8     CS8     EC7     CS7
# Room 2
# CS9     EC9     CS10    EC10
# EC12    CS12    EC11    CS11
# CS13    EC13    CS14    EC14
# EC16    ___     EC15    CS15
