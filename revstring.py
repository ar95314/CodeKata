lst=[]
lst1=[]
class prntrev:
	def string(self,stri):
		for i in stri:
			lst.append(i)
		n=len(lst)
		for i in range(n):
			lst1.append(lst[n-1])
			n=n-1
		for i in range(len(lst1)):
			if i==len(lst1):			
				print(lst1[i])
			else:
				print(lst1[i],end="")
stri=input()
call=prntrev()
call.string(stri)
