N,K=raw_input().split()
N=int(N)
K=int(K)
sum=0
arr=raw_input().split()
for i in range(0,K):
  sum=sum+int(arr[i])
  i+=1
print sum
