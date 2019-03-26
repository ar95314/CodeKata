lst=[]
class ifrepeat:
	def check(self,s):
		flag=0
		temp=s.lower()
		for i in temp:
			if i in lst:
				flag=1
			lst.append(i)
		if flag==1:
			print("No")
		else:
			print("Yes")
s=input()
call=ifrepeat()
call.check(s)
