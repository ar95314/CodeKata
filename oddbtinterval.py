lst=[]
class calculate:
	def oddinterval(self,start,end):
		for i in range(start+1,end):
			if(i%2!=0):
				lst.append(i)
		for i in range(0,len(lst)):
			if i == (len(lst)-1):
				print(lst[i])
			else:
				print(lst[i],end=" ")
start,end=map(int,input().split())
cal=calculate()
cal.oddinterval(start,end)
