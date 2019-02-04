number=int(input())
if number>1:
  for i in range(2,number):
    if(number%i)==0:
      print("no")
      break
  else:
    print("prime number")
else:
  print("no")
