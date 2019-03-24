class sumit:
	def ofdigit(self,n):
		count=0
		while(n>0):
			dig=n%10
			count+=dig
			n=n//10
		print(count)
n=int(input())
call=sumit()
call.ofdigit(n)
