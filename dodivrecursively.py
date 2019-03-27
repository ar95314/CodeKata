class dodiv:
	def recursive(self,n):
		if n>0:
			while n%2==0:
				n=n/2
			else:
				print(int(n))
		else:
			print(int(n))
n=int(input())
call=dodiv()
call.recursive(n)
