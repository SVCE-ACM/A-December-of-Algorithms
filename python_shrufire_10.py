def solve(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * matrix[0][i])
        return total
def determinant(order):
    r=c=order
    matrix=[]
    if r==2:
        r1=[]
        r2=[]
        for i in range(r):
            x=int(input('enter the element: '))
            r1.append(x)
        for i in range(r):
            x=int(input('enter the element: '))
            r2.append(x)
        matrix.append(r1)
        matrix.append(r2)
    else:
        r3=[]
        r1=[]
        r2=[]
        for i in range(r):
            x=int(input('enter the element: '))
            r1.append(x)
        for i in range(r):
            x=int(input('enter the element: '))
            r2.append(x)
        matrix.append(r1)
        matrix.append(r2)
        for i in range(r):
            x=int(input('enter the element: '))
            r3.append(x)
        matrix.append(r3)
    print('Determinant: ',solve(matrix, 1))
order=int(input('Enter the order of the matrix: '))
determinant(order)

