a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
co=0
for i in range(0,1001):
    if (a*i**3 + b*i**2 + c*i + d)/(i-e) == 0:
        co+=1
print(co)