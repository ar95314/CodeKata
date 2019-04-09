lst1=[]
class change:
	def oddeveplace(self,stri):
		for i in stri:
			lst1.append(i)
		for i in range(len(lst1)):
			if i%2==0:
				t=lst1[i+1]
				lst1[i+1]=lst1[i]
				lst1[i]=t
		for i in range(len(lst1)):
			if i==len(lst1)-1:
				print(lst1[i])
			else:
				print(lst1[i],end="")
stri=input()
call=change()
call.oddeveplace(stri)
