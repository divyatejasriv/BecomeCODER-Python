#A number is called Disarium if sum of its digits powered with their respective positions is equal to the number itself.
def disarium(num):
    c=0
    a=0
    temp=num
    while num>0:
        r=num%10
        num=num//10
        c+=1
    num=temp
    while temp>0:
        r=temp%10
        temp=temp//10
        a+=pow(r,c)
        c-=1
    if a==num:
        print(True)
    else:
        print(False)
num=int(input())
disarium(num)
