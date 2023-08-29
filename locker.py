def loc():
    l=[]
    for i in range(100):
        l.append(0)
    l[1] = 1
    for i in range(2,100):
        for j in range(1,101):
            if j%(i+1) == 0:
                if l[j-1] == 1:
                    l[j-1]=0
                else:
                    l[j-1]=1
    c=0
    d=0   
    for i in range(100):
        if l[i]==1:
            c=c+1
            print("locker "+str(i+1)+" is open",end="\n")
        else:
            d=d+1
            print("locker "+str(i+1)+" is closed",end="\n")
    print("opened Lockers",c,"closed lockers",d)

loc()