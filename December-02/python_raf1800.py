t1s=[]
t2s=[]
t1a=[]
t2a=[]
condition=""
c=0

def get():
    print("Enter sides of Traingle ABC: ")
    for i in range(0,3):
        x=int(input())
        t1s.append(x)

    print("Enter angles of Traingle ABC: ")
    for i in range(0,3):
        x=int(input())
        t1a.append(x)

    print("Enter sides of Traingle PQR: ")
    for i in range(0,3):
        x=int(input())
        t2s.append(x)
    
    print("Enter angles of Traingle PQR: ")
    for i in range(0,3):
        x=int(input())
        t2a.append(x)

def check():
    global condition
    global c
    AB = int((t1s[0]+t1s[1]))
    BC = int((t1s[1]+t1s[2]))
    AC = int((t1s[2]+t1s[0]))
    PQ = int((t1s[0]+t1s[1]))
    QR = int((t1s[1]+t1s[2]))
    RP = int((t1s[2]+t1s[0]))
    
    if((AB/PQ == BC/QR) and (BC/QR == AC/RP)):
        condition+=" SSS"
        c=1
    if((AB/PQ == AC/RP and t1a[0]==t2a[0]) or (AB/PQ == BC/QR and t1a[1]==t2a[1]) or (BC/QR == AC/RP and t1a[2]==t2a[2])):
        condition+=" SAS"
        c=1
    if(len(set(t1a).intersection(t2a))>=2):
        condition+=" AAA"
        c=1
        
def main():
    get()
    check()
    if c!=1:
        print("Triangles are not similar")
    else:
        print("Traingles are similar by"+condition)

if __name__ == "__main__":
    main()
