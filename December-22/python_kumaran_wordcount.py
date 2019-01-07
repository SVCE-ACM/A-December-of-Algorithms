def freq(str): 
    str = str.split()       
    str2 = [] 
    for i in str:              
        if i not in str2: 
            str2.append(i)
    str2.sort()        
    for i in range(0, len(str2)): 
        print(str2[i], ':', str.count(str2[i])) 
x=input('Enter')
x=x.lower()
freq(x)
