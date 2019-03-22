class time:
	def printhrmin(self,min):
		if min<60:
			print(0," ",min)
		else:
			dig=int(min/60)
			minit=min-(dig*60)
			print(dig,"",minit)
min=int(input())
call=time()
call.printhrmin(min)
