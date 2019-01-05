def ClosestCell(mat):
    cell = []
    for i, row in enumerate(mat):
        for j, col in enumerate(list(row)):
            if col == '1':
                px = i
                py = j
            if col == '2':
                cell.append((i, j))
    mat2 = []
    for x, y in cell:
        no_wrap = abs(px - x) + abs(py - y)
        col_wrap, row_wrap = abs(px - x) + abs(py - (len(mat) - y)), abs((px + len(mat)) - x) + abs(py-y)
        mat2.append(min(no_wrap, col_wrap, row_wrap))
    return min(mat2) if mat2 else 0

def main():
    mat=[]
    n = int(input("Enter the number of inputs: "))
    for i in range(n):
        mat.append(input())
    print(ClosestCell(mat))

if __name__ == "__main__":
    main()

