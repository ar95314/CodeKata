class printit:
	def findmod(self,a,b,c):
		ans=0
		ans=((a*b)%c)
		print(ans)
a,b,c=map(int,input().split())
call=printit()
call.findmod(a,b,c)
