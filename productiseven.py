class product:
	def iseven(self,n,k):
		temp=n*k
		if temp%2==0:
			print("even")
		else:
			print("odd")
n,k=map(int,input().split())
call=product()
call.iseven(n,k)
