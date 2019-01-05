import random
import time

def Hack(pw,milli):
   
    length = len(pw)
    crack = ""
    count=0
    j=0
    while(1):
        for i in range(32,127):
            if chr(i)==pw[j]:
                crack+=pw[j]
                count+=1
                break
        j+=1
        if count==length and crack==pw:
            break
    print("Milliseconds required: {}".format(int(round(time.time() * 1000))-milli))
    
    
def main():
    milli = int(round(time.time()*1000))
    x = input("Enter password: ")
    Hack(x,milli);
    
if __name__ == "__main__":
    main()
