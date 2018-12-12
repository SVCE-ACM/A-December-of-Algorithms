#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def binary_sort(sort, n, x):
    start = 0
    end = n - 1

    while start <= end:
        mid = int((start + end) / 2)
        if x == sort[mid]:
            return mid
        elif x < sort[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

def main():
 n = int(input("Enter the size of the list: "))
 sort = []
 for i in range(n):
    sort.append(input("Enter {} element: " .format(i+1)))

 x = input("Enter the number to search: ")
 position = binary_sort(sort, n, x)

 if position != -1:
    print("Entered number {} is present at position: {}" .format(x, position+1))
 else:
    print("Entered number {} is not present in the list" .format(x))

if __name__ == '__main__':
      main()
