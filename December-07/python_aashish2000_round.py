def roundno(val,dec,tol,chk):
    print("IsApproximatelyEqual("+str(val)+","+str(dec),end="")
    if(chk==1):
        print(","+str(tol)+") -> ",end="")
    else:
        print(") -> ",end="")


    if(abs(val-dec)<=0.5 and abs(val-dec)<=tol):
        out="True"
    else:
        out="False"
    print(out)

inp=list(map(float,input().split()))
if(len(inp)==2):
    roundno(inp[0],inp[1],inp[0],0)
else:
    roundno(inp[0],inp[1],inp[2],1)

