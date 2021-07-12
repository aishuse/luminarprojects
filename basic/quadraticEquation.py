import cmath

  #  QUADRATIC EQUATION

b=int(input("enter b: "))
a=int(input("enter a: "))
c=int(input("enter c: "))

# d=((b**2)-(4*a*c))**.5
d=cmath.sqrt((b**2)-(4*a*c))
s1=(-b+d)/2*a
s2=(-b-d)/2*a
print("quadratic equation= ",s1 )
print("quadratic equation= ",s2 )
