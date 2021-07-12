print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")

x=int(input("enter which action to perform: "))
def addit(a,b):
    return a+b
def subs(a,b):
    return a-b
def mult(a,b):
    return a*b
def divi(a,b):
    return a/b
a=int(input("enter 1st no: "))
b=int(input("enter 2nd no: "))
if x==1:
    print(a,"+",b,"=",addit(a,b))
if x==2:
    print(a,"-",b,"=",subs(a,b))
if x==3:
    print(a,"*",b,"=",mult(a,b))
if x==4:
    print(a,"/",b,"=",divi(a,b))

