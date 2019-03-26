lst=[]
lst1=[]
class printno:
	def fromstr(self,s):
		for i in s:
			lst.append(i)
		for i in range(len(lst)):
			if lst[i].isdigit():
				lst1.append(lst[i])
		for i in range(len(lst1)):
			print(lst1[i],end="")
s=input()
call=printno()
call.fromstr(s)
