def commonprefix(m):
    if not m:
      return
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c!=s2[i]:
            return s1[:i]
    return s1
  
def main():
    mat=[]
    n = int(input("Enter number of words: "))
    print("Enter words: ")
    for i in range(n):
      x = input()
      mat.append(x)
    pre = commonprefix(mat)
    if pre:
      print("Common prefix: {}".format(pre))
    else:
      print("No Common Prefix")
      

if __name__ == "__main__":
    main()

