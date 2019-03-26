lst=[]
class sort:
	def lexicographical(self,s):
		for i in s:
			lst.append(i)
		lst.sort()
		for i in range(len(lst)):
			print(lst[i],end="")
s=input()
call=sort()
call.lexicographical(s)
