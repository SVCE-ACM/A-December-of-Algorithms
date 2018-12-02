def isLucky(n):
    First_Half = Second_Half = 0
    Ticket_No = int(n)
    Temp = Ticket_No
    Half = int(len(n)/2)
    for i in range(0,Half):
        First_Half += int(n[i])
    for i in range(Half,len(n)):
        Second_Half += int(n[i])
    if(First_Half == Second_Half):
        return 1
    else:
        return 0



def main():
    n=(input("Enter ticket number"))
    if(isLucky(n)):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
