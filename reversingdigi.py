lst=[]
class reverse:
	def digit(self,n):
		dig=0
		while n>0:
			dig=n%10
			lst.append(dig)
			n=n//10
		for i in range(len(lst)):
			if i == len(lst)-1:
				print(lst[i])
			else:
				print(lst[i],end="")
n=int(input())
call=reverse()
call.digit(n)
