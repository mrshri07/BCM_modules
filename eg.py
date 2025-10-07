
'''num = int(input("Enter a number: "))
print("You entered:", num)
length = len(str(num))
print(length)
result = sum(int(digit) ** length for digit in str(num))

print("Result:", result)'''

'''
x=5
y=6
print("before swaping  x=",x)
print("y=",y)
x,y=y,x
print("after swaping x=",x)
print("y=",y)

x=2
y=4
print("before swaping  x=",x)
print("y=",y)
a=x+y
x=a-x
y=a-x
print("after swaping x=",x)
print("y=",y)



x=8
y=4
print("before swaping  x=",x)
print("y=",y)
a=x*y
x=a/x
y=a/x
print("after swaping x=",x)
print("y=",y)'''

"""
x="my name is sreyas krishnan a s"
print(x)
print(x[::-1])
"""
'''
arr = [5,8,9,15,22,75,85,700, 2, 29, 1, 6]
arr.sort()
print("Sorted Array:", arr)'''

"""

n = 158
b = 0
k=n
while n > 0:
    m = n % 10
    b = b + (m ** 3)
    n = n //10
print("b=",b)


if b==k:
     print("It is an Armstrong number")
else:
     print("Not an Armstrong number")"""


'''

n = 151

b = 0
k=n
while n > 0:
    m = n % 10

    b = b*10+ m
    n = n //10
print("b=",b)


if b==k:
     print("It is an pallindrom number")
else:
     print("Not an pallindrom number")





b = 0
n = 15100
k = n
while n > 0:
   m = n % 10
   b = b*10+m
   n =n//10

print(b)
if b==k:
     print("It is an pallindrom number")
else:
     print("Not an pallindrom number")
'''

# print("100" "200")
# name="sreyas"
# age=25
# print("my name is",name,"i am",age,"years old")
# print(f"my name is {name} iam {age} years old")
# num=1
# i=2
# limit=100
# while i<=limit:
#     if num%i==0:
#         for(i in range (100)):
#         print(num)
#       # print("num is not prime")
#        break
#     i=i+1
# else:
#      print("prime")
# def function(fx):
#     print(fx +" "+"hello")
# function("y")
# function("z")
# myname=input("enter the name")
# number=tuple(input("enter the list"))
# print(number)
# print(myname)
def fact(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    print(f"fact of {n} = {result}")
    return result
fact(5)


nums = [10, 4005, 5282, 99, 100,555]
print(nums)
num=(max(nums))
nums.remove(num)
print(nums)
num=(max(nums))
print(f"second largest number={num}")