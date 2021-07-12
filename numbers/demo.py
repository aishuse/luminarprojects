#
#
# n=int(input("enter a number:"))
# s=0
# count=len(str(n))
# print(count)
#
# def happy(n):
#     s=0
#     for j in range(0,count):
#
#             a=n%10
#             s=s+a**2
#             n=n//10
#     # print(s, end=" ")
#     # print("\n")
#     return s
#
#
# for i in range(0,count):
#     s=happy(n)
#     print(s)
#     # happy(s)
#
#
#

# isHappyNumber() will determine whether a number is happy or not
# def isHappyNumber(num):
rem = sum = 0;
num = 32;
result = num;

    # Calculates the sum of squares of digits
while (num > 0):
        rem = num % 10;
        sum = sum + (rem * rem);
        num = num // 10;
print(sum)
# return sum;




# while (result != 1 and result != 4):
#     result = isHappyNumber(result);

# Happy number always ends with 1
if (result == 1):
   print(str(num) + " is a happy number");
# Unhappy number ends in a cycle of repeating numbers which contain 4
elif (result == 4):
   print(str(num) + " is not a happy number");