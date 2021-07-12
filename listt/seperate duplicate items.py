a = [10,20,30,20,10,50,60,40,80,50,40]
s=set()
l=[]
print(len(l))
if len(l)==0:
    print("list empty")


for i in a:
    if i not in s:
        s.add(i)
    else:
        l.append(i)

print(l)
print(s)
