class finddiff:
	def problem(self,n,m):
		diff=m-n
		#given always kabali clan is less than opponent
		print(diff)
#n-no of ninjas in kabali clan and y-ninjas in opponent clan
n,m=map(int,input().split())
call=finddiff()
call.problem(n,m)
