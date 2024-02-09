# to check if the number entered by user is odd or even
number =int(input("Enter the number"))
if(number%2==0):
  print("It is EVEN");

else:
  print("It is ODD");

# wap to find the greatest of 3 numbers entered by user
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if(num1>num2 and num1>num3):
  print("num1 is greater")

if(num2>num1 and num2>num3):
  print("num2 is greater")

if(num3>num2 and num3>num1):
  print("num3 is greater")

# wap to check whether the number entered by user is a multiple of 7 or not
num7=int(input("Enter the number"))
if(num7%7==0):
  print("It is a multiple of 7")

else:
  print("It is not a multiple of 7")