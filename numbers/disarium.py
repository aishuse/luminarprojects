num = int(input("Enter number: "))
l=(len(str(num)))
dis=num
s=0

while num>0:
    a=num%10
    s=s+a**l
    num=num//10
    l-=1
if s==dis:
    print( "Disarium ")
else:
    print("not")

#
length=0
def sumOfDigits(num):
    sum=0
    length=len(str(num))

    while (num > 0):
        rem = num % 10;
        sum = sum + (rem ** length);
        num = num // 10;
        length = length - 1;
    return sum;

result = 0;
print("Disarium numbers between 1 and 100 are");
for i in range(1, 200):
    result = sumOfDigits(i);

    if (result == i):
        print(i),
