def  game(n,f=[]):
    x=0
    c=0
    p=[]
    a=0
    w=""
    l="String to run the while loop"
    for i in range (n):
        for j in range (n):
            p.append(x)
            x+=1
        
    while (l!=""):
        for i in range (n*n):           
            print (p[i], end="")
            if ((i+1)%n==0):
                print ()
    
        if (a%2==0):
            y=f[a]
            print ("X-->",y)
            z="X"
        else:
            y=f[a]
            print ("O-->",y)
            z="O"
        a+=1
        p[y]=update(y,z,p)
        w,c=Winner(n,p)
        if (w!=""):
            for j in range (n*n):           
                print (p[j], end="")
                if ((j+1)%n==0):
                    print ()
            print ("Winner: "+w)
            break
        if c==n*n:
            for j in range (n*n):           
                print (p[j], end="")
                if ((j+1)%n==0):
                    print ()
            print ("Winner: None")
            break
    
def update (y,z,p):
    if (z=="X") :
        p[y]="X"
    elif (z=="O") :
        p[y]="O"
    return p[y]

def Winner (n,p):
    winner=""
    cx1=0
    co1=0
    cx2=0
    co2=0
    for i in range (0,n*n):#diagnols
        if (i%(n+1)==0):
            if (p[i]=="X"):
                cx1+=1
            elif(p[i]=="O"):
                co1+=1
        if (i%(n-1)==0 and i!=0 and i/(n-1)<=n):
            if (p[i]=="X"):
                cx2+=1
            elif(p[i]=="O"):
                co2+=1
    t=0
    for k in range (0,n):#Vertical
        cx3=0
        co3=0
        u=n
        for i in range(0,n):
            if p[k+(u*i)]=="X":
                cx3+=1
            elif(p[k+(u*i)]=="O"):
                co3+=1
        if (cx3==n or co3==n) :
            break 
    for r in range (0,n*(n-1)+1,n):#Horizaontal
        cx4=0
        co4=0
        for c in range (0,n):    
            if (p[r+c]=="X"):
                cx4+=1
            elif(p[r+c]=="O"):
                co4+=1 
        if (cx4==n or co4==n) :
            break      
        
    if(cx1==n or cx2==n or cx3==n or cx4==n):
        winner="X"
    if(co1==n or co2==n or co3==n or co4==n):
        winner="O"
    c=0
    for i in range (0,n*n):
        if p[i]=="X" or p[i]=="O":
            c+=1  
    return winner,c            
        
def main ():
    n=3
    c=[]

    y=input()
    c=y.split('->')
    f=[]
    for i in range(len(c)):
        x=0
        if c[i]=="(0,0)":
           x=0
        elif c[i]=="(0,1)":
            x=1
        elif c[i]=="(0,2)":
            x=2
        elif c[i]=="(1,0)":
            x=3
        elif c[i]=="(1,1)":
            x=4
        elif c[i]=="(1,2)":
            x=5
        elif c[i]=="(2,0)":
            x=6
        elif c[i]=="(2,1)":
            x=7
        elif c[i]=="(2,2)":
            x=8        
        f.append(x)
    game(n,f)
main () 
