def factorial(num):
  if num==1:
    return num
  else:
    return num*factorial(num=1)
num=int(input(1))
if num<0:
    print()
elif num==0:
    print("factorial of 0 is 1")
else:
    print(factorial(num))
