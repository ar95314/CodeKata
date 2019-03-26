class printK:
	def val(self,n,k,lst):
		for i in range(1,n):
			if i==k:
				print(lst[i-1])
				break
n,k=map(int,input().split())
lst=list(map(int,input().split()))
call=printK()
call.val(n,k,lst)
