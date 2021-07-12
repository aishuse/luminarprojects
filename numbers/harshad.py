n=int(input("enter a number: "))
s=0
x=n
# while n>0:
while n>0:
    # x=n
    a=n%10
    s=s+a
    n=n//10
print(s)
print(x)
if x%s==0:
    print("harshad")
else:
    print("not")



def harsh(n):
    s=0
    while n > 0:
        a=n%10
        s=s+a
        n=n//10
    return s

for i in range(1,50):
    x=harsh(i)
    if i%x==0:
        print(i)
