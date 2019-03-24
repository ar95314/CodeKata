class checknear:
	def muloften(self,n):
		if n%10==0:
			print(n)
		else:
			n=n+(10-(n%10))
			print(n)
n=int(input())
call=checknear()
call.muloften(n)
