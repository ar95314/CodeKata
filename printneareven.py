class neareven:
	def printeven(self,n):
		for i in range(0,n+1):
			n1=n-i
			if n1%2==0:
				print(n1)
				break
n=int(input())
call=neareven()
call.printeven(n)
