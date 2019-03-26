class sumn:
	def do(self,n,lst):
		sum=0
		for i in range(0,n):
			sum+=lst[i]
		print(sum)
n=int(input())
lst=list(map(int,input().split()))
call=sumn()
call.do(n,lst)
