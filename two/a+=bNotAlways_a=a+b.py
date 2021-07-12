import operator

a=2
b=10
#a+=b
print(operator.iadd(a,b))
print(a)

list=[1,2,3,4]
list2=list
print(list2)
list+=[7,8,9]
print(list2)
print(list)