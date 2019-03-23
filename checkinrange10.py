lst=[]
class checkno:
	def inrange(self,n):
		for i in range(1,11):
			lst.append(i)
		if n in lst:
			print("yes")
		else:
			print("no")
n=int(input())
call=checkno()
call.inrange(n)
		
