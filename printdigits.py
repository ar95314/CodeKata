class number:
	def printit(self,n):
		for i in range(len(n)):
			if i == (len(n)-1):
				print(n[i])
			else:
				print(n[i],end=" ")
n=input()
call=number()
call.printit(n)
