lst=[]
sum=0
no=input()
n,k=no.split()
for i in range(0,n):
  data=int(input())
  lst.append(data)
for i in range(0,k):
  sum+=lst[i]
print(sum)
