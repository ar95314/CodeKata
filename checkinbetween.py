class checkif:
	def inbetween(self,n,l,r):
		if l<n and n<r:
			print("yes")
		else:
			print("no")
n=int(input())
l,r=map(int,input().split())
call=checkif()
call.inbetween(n,l,r)
