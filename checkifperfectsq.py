class check:
	def ifperfect(self,n,m):
		prod=n*m
		if n==m:
			print("yes")
		else:
			print("no")
n,m=map(int,input().split())
call=check()
call.ifperfect(n,m)
