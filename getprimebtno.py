lst1=[]
class getprime:
  def prime(self,n,m):
  	for i in range(n+1,m):
  		for j in range(2,i):
  			if i%j==0:
  				break
  		else:
  			lst1.append(i)
  	for i in range(len(lst1)):
  		if i==len(lst1)-1:
  			print(lst1[i])
  		else:
  			print(lst1[i],end=" ")
n,m=map(int,input().split())
c=getprime()
c.prime(n,m)
