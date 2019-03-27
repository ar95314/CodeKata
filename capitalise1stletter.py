lst=[]
class capitalise:
	def firstletter(self,s):
		for i in s:
			lst.append(i)
		for i in range(len(lst)):
			lst[0]=lst[0].upper()
			if lst[i]==" ":
				lst[i+1]=lst[i+1].upper()
		for i in range(len(lst)):
			print(lst[i],end="")
s=input()
call=capitalise()
call.firstletter(s)
