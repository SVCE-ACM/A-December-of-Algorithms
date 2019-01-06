import sys
import operator
def wcount(filename):
    f=open(filename,'r')
    word=f.read().lower().replace("."," ").replace(","," ").split()
    w=sorted(word) 
    wc={x:w.count(x) for x in w}
    return wc

def print_words(filename):
    printw=wcount(filename).items()
    for x,y in printw:
        print(x,  y)
        
def print_top(filename):
     s=sorted(wcount(filename).items(),key=operator.itemgetter(1),reverse=True)
     for x in range (0,20):
        print(s[x][0],s[x][1])
def main():
  if len(sys.argv) != 3:
    file=open("wordcount.txt",'w')
    string=input("enter string(s)")
    file.write(string)
    file.close()  
    print('cmd usage: python python_AkshayaRC.py {--count | --topcount} wordcount.txt')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
