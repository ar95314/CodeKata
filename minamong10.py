class arrayof10:
	def min(self,lst):
		min=lst[0]
		for i in range(0,len(lst)):
			if min > lst[i]:
				min=lst[i]
		print(min)
lst=list(map(int,input().split()))
call=arrayof10()
call.min(lst)
