# Dec 15
mat = []
row = []
r = int(input("Enter the number of rows "))
mat.append([1])
if r == 1:
    mat.append([1, 1])
elif r > 1:
    prev = [1, 1]
    mat.append(prev)
    for i in range(1, r):
        for j in range(len(prev)-1):
            row.append(prev[j]+prev[j+1])
        row.insert(0, 1)
        row.append(1)
        mat.append(row.copy())
        prev = row.copy()
        row.clear()
p1 = len(mat)-1
p2 = 0
poly = ""
for i in range(len(mat)):
    for x in mat[i]:
        print(x, end=" ")
    print(f" --> row {i}")
for i in range(len(mat)):
    val = mat[r][i]
    poly = poly + f"({val}x^{p1}y^{p2})+"
    p1 -= 1
    p2 += 1
print("Polynomial: ", poly[:-1])

# Sample I/O
# Enter the number of rows 3
# 1  --> row 0
# 1 1  --> row 1
# 1 2 1  --> row 2
# 1 3 3 1  --> row 3
# Polynomial:  (1x^3y^0)+(3x^2y^1)+(3x^1y^2)+(1x^0y^3)
