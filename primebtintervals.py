class calprime:
	def prime(self,start,end):
		for num in range(start+1,end):
			for i in range(2,num):
				if num%i==0:
					break
			else:
				if num==(end-1):
					print(num)
				else:
					print(num,end=" ")
start,end=map(int,input().split())
c=calprime()
c.prime(start,end)
