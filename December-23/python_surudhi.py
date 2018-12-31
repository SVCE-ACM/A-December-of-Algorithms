n=int(input('Number of classrooms: '))
size=int(input('Size of classrooms (1-50): '))
no_of_dept=int(input('Enter the number of departments: '))
dept=[]
strn=[]
s=[]
for i in range(no_of_dept):
    print('Department',i+1,'Code: ')
    s=input()
    dept.append(s)
for i in range(no_of_dept):
    s=print('Students in department',i+1,': ')
    s=input()
    strn.append(s)
col=no_of_dept*2
row=size//col
y=[]

def printseat(row,no_of_dept):
    c=0
    s=1
    for i in range(n):
        print("class",i+1,'\n')
        for k in range(size//n):
            for j in range(no_of_dept):
                print(dept[j],(k+1)+c,'\t',end='')
            if((k+1)+c==(no_of_dept)*s):
                print('\n')
                s=s+1
                if j+1<no_of_dept:
                    temp=dept[j]
                    dept[j]=dept[j+1]
                    dept[j+1]=temp
                else:
                    temp=dept[j]
                    dept[j]=dept[j-1]
                    dept[j-1]=temp
        c=c+(col*no_of_dept)
        print('\n')
printseat(row,no_of_dept)

