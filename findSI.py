lst=[]
class calculate:
	def SI(self,p,t,r):
		si=(p*r*t)/100
		print(int(si))
p,t,r=map(int,input().split())
call=calculate()
call.SI(p,t,r)
