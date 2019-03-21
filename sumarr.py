lst=[]
sum=0
n,k=map(int,input().split())
lst=list(map(int,input().split()))
for i in range(0,k):
  sum+=lst[i]
print(sum)
