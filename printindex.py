class array:
	def printindex(self,lst,n):
		for i in range(0,n):
			print(lst[i],i)
n=int(input())
lst=list(map(int,input().split()))
call=array()
call.printindex(lst,n)
