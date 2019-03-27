class printlast:
	def nchar(self,n,str):
		leng=len(str)
		n=int(n)
		while n>0:
			print(str[leng-n],end="")
			n=n-1
str,n=map(str,input().split())
call=printlast()
call.nchar(n,str)
