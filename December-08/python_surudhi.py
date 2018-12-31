def SingularPlural(z,num):
    k=[]
    if num>1:
        if z[-1]in['s','x','z','ch','sh']:k=z+'es'
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
        elif z[-2:]=='es'and z[-3]not in['a','e','i','o','u']:k=z[:-1]
        elif z[-2:]=='es':k=z[:-2]
        else:k=z
    return k
str1=input('Enter the first string: ')
c=input('Second character is string or number?(S/N): ')
if c=='S':
    str2=input('Enter the second string: ')
    if str2[-1]=='s':
          a=SingularPlural(str2,1)
          print(a)
          if a==str1:
              print('Singular:',str1,'\nPlural:',str2)
          else:
              print('Invalid Input')
    else:
          a=SingularPlural(str2,2)
          if a==str1:
              print('Singular:',str2,'\nPlural:',str1)
          else:
              print('Invalid Input')
elif c=='N':
    num=int(input('Enter the number: '))
    print(SingularPlural(str1,num))
