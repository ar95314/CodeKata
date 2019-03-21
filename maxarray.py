class array:
	def max(self,n,lst):
		max=lst[0]
		for i in range(0,n):
			if max < lst[i]:
				max=lst[i+1]
		print(max)
n=int(input())
lst=list(map(int,input().split()))
call=array()
call.max(n,lst)
