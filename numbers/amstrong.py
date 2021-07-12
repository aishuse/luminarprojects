# # Program to check Armstrong numbers in a certain interval
#
# lower = 100
# upper = 2000
#
# for num in range(lower, upper + 1):
#
#     # order of number
#     order = len(str(num))
#
#     # initialize sum
#     sum = 0
#
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#
#     if num == sum:
#         print(num)
#
#
#
n= int(input("Enter a number: "))
ams=n
sum=0
while n>0:
   a=n%10
   sum=sum+a**3
   n=n//10
if sum==ams:
   print("armstrong")
else:
   print("not")


#
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))

for num in range(0, 200):
   sum = 0
   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //= 10
      if num == sum:
         print(num)


