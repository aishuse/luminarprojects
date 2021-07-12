l1=[]
l2=[]
for i in range(0,11):
    l1.append(4*i)
for i in range(0,10):
    l2.append(l1[i]%5==0)
print(all(l2))

list1=[]
list2=[]
# == , is
print("next == is pgm")
list3=list1
if(list2==list1):
    print("True")
else:
    print("false")
if(list2 is list1):
    print("true")
else:
    print("false")

if(list3 == list1):
    print("true")
else:
    print("false")

if(list3 is list1):
    print("true")
else:
    print("false")