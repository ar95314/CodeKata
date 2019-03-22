class time:
	def printhrmin(self,min1,hr1,min2,hr2):
		hr=abs(hr1-hr2)
		min=abs(min1-min2)
		print(hr,min)
hr1,min1=map(int,input().split())
hr2,min2=map(int,input().split())
call=time()
call.printhrmin(min1,hr1,min2,hr2)
