lst=[]
class calculate:
	def areavol(self,l,b,h):
		tsa=vol=0
		tsa=2*((l*b)+(b*h)+(h*l))
		vol=(l*b*h)
		lst.append(tsa)
		lst.append(vol)
		for i in range(len(lst)):
			if i == len(lst)-1:
				print(lst[i])
			else:
				print(lst[i],end=" ")
l,b,h=map(int,input().split())
call=calculate()
call.areavol(l,b,h)
