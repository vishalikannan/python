s,e=raw_input().split()
s=int(s)
e=int(e)
for i in range(s+1,e):
  a=0
  temp=i
  while i>0:
    rem=i%10
    a=a+rem**3
    i=i//10
  if temp==a:
    print a
