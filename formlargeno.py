lst1=[]
class formlarge:
	def no(self,n,lst):
		c=0
		lst.sort(reverse=True)
		for i in lst:
			c+=i
		if c==0:
			print(0)
		else:
			for i in range(len(lst)):
				if i==len(lst)-1:
					print(lst[i])
				else:
					print(lst[i],end="")
n=int(input())
lst=list(map(int,input().split()))
call=formlarge()
call.no(n,lst)
