class checkpwr:
	def ifpwr2(self,n):
		if n==1:
			print("yes")
		elif n%2==0:
			print("yes")
		else:
			print("no")
n=int(input())
call=checkpwr()
call.ifpwr2(n)
