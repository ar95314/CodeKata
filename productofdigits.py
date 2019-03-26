class product:
	def ofdigit(self,n):
		count=1
		while(n>0):
			dig=n%10
			count*=dig
			n=n//10
		print(count)
n=int(input())
call=product()
call.ofdigit(n)
