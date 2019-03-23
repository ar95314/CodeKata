class printstr:
	def ntimes(self,n,str):
		for i in range(int(n)):
			print(str)
str,n=map(str,input().split())
call=printstr()
call.ntimes(n,str)
