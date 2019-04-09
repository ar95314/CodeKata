lst1=[]
class checkprime:
  def prime(self,n,m):
  	count=0
  	for i in range(n,m+1):
  		for j in range(2,i):
  			if i%j==0:
  				break
  		else:
  			count+=1
  	print(count)
n,m=map(int,input().split())
c=checkprime()
c.prime(n,m)
