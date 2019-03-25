import math
class check:
	def ifperfect(self,n):
		temp=int(math.sqrt(n))
		if temp*temp == n:
			print("yes")
		else:
			print("no")
n=int(input())
call=check()
call.ifperfect(n)
