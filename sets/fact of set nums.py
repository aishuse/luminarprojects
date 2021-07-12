s=set()
for i in range(1,5):
    s.add(i)
print(s)
f=set()

for x in s:
    n=1
    for i in range(1,x+1):
        for j in range(1,i+1):
            n=n*i
            break
    f.add((n))

print(f)