class findavg:
	def calculateavg(self,n,lst):
		tot=avg=0
		for i in range(n):
			tot+=lst[i]
		avg=tot/n
		print(int(avg))
n=int(input())
lst=list(map(int,input().split()))
call=findavg()
call.calculateavg(n,lst)
