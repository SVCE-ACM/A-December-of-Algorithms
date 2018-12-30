def Hanoi(n,first,mid,last):
    if n >= 1:
        Hanoi(n-1,first,last,mid)
        print(first,"=>",last)
        Hanoi(n-1,mid,first,last)

n=int(input("enter no.of disks: "))
Hanoi(n,'left','middle','right')
