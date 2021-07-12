s=set()
for i in range(0,10):
    s.add(i)
print(s)
nonprime=set()
prime=set()
for i in s:
    for j in range(2,i):
        if i%j==0:
            nonprime.add(i)
            break
    else:
        prime.add(i)
print(nonprime)
print(prime)