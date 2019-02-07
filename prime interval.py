n,k=raw_input().split()
n=int(n)
k=int(k)
for i in range(n+1,k):
   j=0
   if i>1:
      for s in range(2,i):
        if i%s==0:
          j=j+1
   if j<=0:
      print i,
