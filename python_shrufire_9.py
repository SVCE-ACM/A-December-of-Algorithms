import re
def IsURL(str1):
    p = re.search('^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$', str1) 
    if p:
        print('True')
    else:
        print('False')

str1 = input('Enter the URL: ')
IsURL(str1)


        
