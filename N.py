p,n,z=0,0,0
for i in range(int(input())):
    num=int(input())
    if num>0:
        p+=1
    elif num<0:
        n+=1
    else:
        z+=1
print(z,p,n)