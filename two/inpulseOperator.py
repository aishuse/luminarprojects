# list1 = [10,11,23,45]
# list2 = list1
#
# # print("2nd list : ",list2)
# # list1 += [1, 2, 3, 4]
# # print(list2)
# # print(list1)
# print("next")
# list1=list1+[1,2,3,4]
#
# print(list1)
# print(list2)

# Python code to demonstrate difference between
# Inplace and Normal operators in Immutable Targets

# importing operator to handle operator operations
import operator

# Initializing values
x = 5
y = 6
a = 5
b = 6

# using add() to add the arguments passed
z = operator.add(a,b)

# using iadd() to add the arguments passed
p = operator.iadd(x,y)

# printing the modified value
print ("Value after adding using normal operator : ",end="")
print (z)

# printing the modified value
print ("Value after adding using Inplace operator : ",end="")
print (p)

# printing value of first argument
# value is unchanged
print ("Value of first argument using normal operator : ",end="")
print (a)

# printing value of first argument
# value is unchanged
print ("Value of first argument using Inplace operator : ",end="")
print (x)

#########################

alist=[1,2,3,4,5]
z=operator.add(alist,[7,8,9])
print("z is ",z)
print("alist is ",alist)

iad=operator.iadd(alist,[7,8,9])
print("iad is ",iad)
print("alist is ",alist)
