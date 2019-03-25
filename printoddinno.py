lst=[]
lst1=[]
class printodd:
	def call(self,n):
		while(n>0):
			n1=n%10
			lst.append(n1)
			n=n//10
		for i in range(len(lst)):
			if lst[i]%2!=0:
				lst1.append(lst[i])
		for i in range(len(lst1)):
			if i==(len(lst1))-1:
				print(lst1[i-1])
			else:
				print(lst1[i+1],end=" ")
n=int(input())
call=printodd()
call.call(n)
