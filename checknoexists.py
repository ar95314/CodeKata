class checkif:
	def noexists(self,n,k,lst):
		count=0
		for i in range(n):
			if k==lst[i]:
				count+=1
		if count>0:
			print("yes")
		else:
			print("no")
n,k=map(int,input().split())
lst=list(map(int,input().split()))
call=checkif()
call.noexists(n,k,lst)
