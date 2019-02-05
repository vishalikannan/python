n=int(raw_input())
arms=0
temp=n
while n>0:
  rem=n%10
  arms=arms+rem**3
  n=n/10
if temp==arms:
  print"yes"
else:
  print"no"
