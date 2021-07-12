x=int(input("enter a num: "))
y=int(input("enter a num: "))
if x>y:
    great=x
else:
    great=y
lcm=0
while(True):
    if great%x==0 and great%y==0:
        lcm=great
        break

    great+=1
print(lcm)

