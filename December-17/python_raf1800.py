import numpy as np

def printer(matrix):
    print("\n".join(str(x) for x in matrix))
    print()
    
def MS(r):
    matrix = np.zeros((r,r), dtype=int)
    n = 1
    i, j = 0, r//2
    while n <= r**2:
        matrix[i, j] = n
        n += 1
        newi=(i-1)%r
        newj=(j+1)%r
        if matrix[newi, newj]:
            i+=1
        else:
            i=newi
            j=newj
    printer(matrix)
    printer(np.flip(matrix,1))
    printer(matrix[::-1])
    printer(np.flip(matrix))
    matrix = matrix.transpose()
    printer(matrix)
    printer(np.flip(matrix,1))
    printer(matrix[::-1])
    printer(np.flip(matrix))
    
def main():
    x = int(input("Enter number of rows: "))
    MS(x);
    
if __name__ == "__main__":
    main()
