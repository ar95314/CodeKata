lst=[]
class multiply:
	def fivemul(self,n):
		for i in range(1,6):
			lst.append(i*n)
		for i in range(0,len(lst)):
			if lst[i]==lst[len(lst)-1]:
				print(lst[i])
			else:
				print(lst[i],end=" ")
n=int(input())
call=multiply()
call.fivemul(n)
