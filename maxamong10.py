class arrayof10:
	def max(self,n,lst):
		max=lst[0]
		for i in range(0,n):
			if max < lst[i]:
				max=lst[i]
		print(max)
n=10
lst=list(map(int,input().split()))
call=arrayof10()
call.max(n,lst)
