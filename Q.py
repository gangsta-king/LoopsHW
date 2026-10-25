a,b,c,d=int(input()),int(input()),int(input()),int(input())
s=[]
for i in range(0,1001):
    if a*i**3 + b*i**2 + c*i + d == 0:
        s.append(i)
print(*s[::-1])