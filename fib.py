lst=[]
class fib:
	def create(self,n):
		fib=0
		a=b=1
		lst.append(a)
		lst.append(b)
		while(n-2):
			fib=a+b
			a=b
			b=fib
			lst.append(fib)
			n=n-1
		for i in range(len(lst)):
			if lst[i]==lst[len(lst)-1]:
				print(lst[i])
			else:
				print(lst[i],end=" ")
n=int(input())
call=fib()
call.create(n)
