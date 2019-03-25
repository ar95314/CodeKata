lst=[]
class printfact:
	def ofno(self,n):
		for i in range(1,n+1):
			if n%i==0:
				lst.append(i)
		for i in range(len(lst)):
			if i==(len(lst))-1:
				print(lst[i])
			else:
				print(lst[i],end=" ")
n=int(input())
c=printfact()
c.ofno(n)
