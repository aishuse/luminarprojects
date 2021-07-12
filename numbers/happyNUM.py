def happy(num):
    s=0
    while num>0:
        a=num%10
        s=s+a**2
        num=num//10
    return s

num=82

r=num

while(r!=1 and r!=4):
    r=happy(r)

if r==1:
    print("happy")
else:
    print("not")
