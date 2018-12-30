def vowsq(StrArr):
  vocal='aeiou'
  for x in range (0,len(StrArr)-1):
    for y in range(0,len(StrArr[x])-1):
      if(vocal.find(StrArr[x][y])>-1):
        if(vocal.find(StrArr[x][y+1])>-1):
          if(vocal.find(StrArr[x+1][y])>-1):
            if(vocal.find(StrArr[x+1][y+1])>-1):
              return(str(x)+'-'+str(y))
  return("Unavailable")

def main():
    mat=[]
    n = int(input("Enter number of words: "))
    print("Enter words: ")
    for i in range(n):
      x = input()
      mat.append(x)
    print(vowsq(mat))

if __name__ == "__main__":
    main()

