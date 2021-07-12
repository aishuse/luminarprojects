x=65
for i in range(0,5):
    for j in range(0,i+1):
        ch=chr(x)
        print(ch,end=" ")
        x=x+1
    print("\r")

x = 65
for i in range(0, 5):
    for j in range(0, i + 1):
        ch = chr(x)
        print(ch, end=" ")
    x = x + 1
    print("\r")
