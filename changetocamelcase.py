lst1=[]
class change:
	def tocamelcase(self,stri):
		for i in stri:
			lst1.append(i)
		lst1[0]=lst1[0].upper()
		for i in range(1,len(lst1)):
			lst1[i]=lst1[i].lower()
			if lst1[i]==" ":
				lst1[i+1]=lst1[i+1].upper()
				pos=i+2
				break
		for i in range(pos,len(lst1)):
			lst1[i]=lst1[i].lower()
		for i in range(len(lst1)):
			if i==len(lst1)-1:
				print(lst1[i])
			else:
				print(lst1[i],end="")
stri=input()
call=change()
call.tocamelcase(stri)
