import sys
def IdDia(mat,m,n):
    for i in range(m-1):
        for j in range(n-1):
            if(mat[i][j]!=mat[i+1][j+1]):
                print("Diagonals Unidentical")
                sys.exit(0)
    print("Diagongals Identical")

def main():
    mat=[]
    m=int(input("Enter number of rows: "))
    n=int(input("Enter number of columns: "))
    for i in range(m):
        mat.append([0]*n)
    print("Enter the elements:")
    for i in range(m):
        for j in range(n):
            mat[i][j]=int(input())
    IdDia(mat,m,n)
    
if __name__ == "__main__":
    main()

