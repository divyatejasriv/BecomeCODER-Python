num=int(input())
rev=0
l=num%10
c=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
    c+=1
rev=rev%pow(10,c-1)
rev=rev//10
rev=rev*10+l
rev=r*pow(10,c-1)+rev
print(rev)
