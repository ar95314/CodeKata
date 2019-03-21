lst=[]
class calprime:
	def prime(self,start,end):
		for num in range(start+1,end):
			for i in range(2,num):
				if num%i==0:
					break
				
			else:
				lst.append(num)
		for i in range(0,len(lst)):
			if i == (len(lst)-1):
				print(lst[i])
			else:
				print(lst[i],end=" ")
start,end=map(int,input().split())
c=calprime()
c.prime(start,end)
