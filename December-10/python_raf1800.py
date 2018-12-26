def det2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def det(matrix):
    a,b,c = matrix[0]
    uno = [x[1:] for x in matrix[1:]]
    dos = [x[::2] for x in matrix[1:]]
    tres = [x[0:2] for x in matrix[1:]]
    det = (
        a * det2x2(uno)
        - b * det2x2(dos)
        + c * det2x2(tres)
    )
    return det

def main():
    m = []
    n=int(input("Enter number of rows: "))
    for i in range(n):
        m.append([0] * n)
    print("Enter the matrix value")
    for i in range(n):
        for j in range(n):
            m[i][j]=int((input("Value: ")))
    if n==2:
        print("Determinant: {}".format(det2x2(m)))
    else:
        print("Determinant: {}".format(det(m)))
    
if __name__ == "__main__":
    main()
