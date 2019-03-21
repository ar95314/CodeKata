class array:
	def min(self,n,lst):
		min=lst[0]
		for i in range(0,n):
			if min > lst[i]:
				min=lst[i]
		print(min)
n=int(input())
lst=list(map(int,input().split()))
call=array()
call.min(n,lst)
