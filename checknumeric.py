class check:
	def numeric(self,n):
		if n.isdigit():
			print("yes")
		else:
			print("No")
n=input()
call=check()
call.numeric(n)
