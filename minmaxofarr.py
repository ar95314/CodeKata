class findminmax:
	def calculate(self,n,lst):
		print(min(lst),max(lst))
n=int(input())
lst=list(map(int,input().split()))
call=findminmax()
call.calculate(n,lst)
