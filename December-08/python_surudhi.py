def SingularPlural(z,num):
    k=[]
    if type(num)==int:
        if num>1:
            if z[-1]in['s','x','z'] or z[-2:]in['ch','sh','ss']:k=z+'es'
            elif z[-1]=='y'and z[-2]not in['a','e','i','o','u']:k=z[:-1]+'ies'
            elif z[-2:]=='fe':k=z[:-2]+'ves'
            elif z[-1]=='f':k=z[:-1]+'ves'
            elif z[-1]=='o'and z[-2]not in['a','e','i','o','u']:k=z[:-1]+'oes'
            else:k=z+'s'
        if num==1 or num==-1:
            if z[-3:]=='ies':k=z[:-3]='y'
            elif z[-3:]=='ves' and z[-4]not in['a','e','i','o','u']:k=z[:-3]='f'
            elif z[-3:]=='ves':k=z[:-3]='fe'
            elif z[-3:]=='oes' and z[-4]not in['a','e','i','o','u']:k=z[:-3]='o'
            elif z[-2:]=='es'and z[-3]not in['a','e','i','o','u']:k=z[:-2]
            elif z[-2:]=='es':k=z[:-2]
            else:k=z
    elif type(num)==str:
        if num[-1]=='s':
            a=SingularPlural(num,1)
            if a==z:
                print('Singular:',z,'\nPlural:',num)
            else:
                print('Invalid Input')
        else:
            a=SingularPlural(num,2)
            if a==z:
                print('Singular:',num,'\nPlural:',z)
            else:
                print('Invalid Input')
    return k
str1=input('Input 1: ')
str2=input('Input 2: ')
if str2.isdigit()==True:
    print(SingularPlural(str1,int(str2)))
else:
    SingularPlural(str1,str2)      
