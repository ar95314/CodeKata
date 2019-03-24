class repitation:
	def printno(self,n,k,lst):
		count=0
		for i in range(n):
			if k==lst[i]:
				count+=1
		print(count)
n,k=map(int,input().split())
lst=list(map(int,input().split()))
call=repitation()
call.printno(n,k,lst)
