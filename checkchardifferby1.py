lst1=[]
lst2=[]
class checkchar:
	def differby1(self,str1,str2):
		c=0
		for i in str1:
			lst1.append(i)
		for i in str2:
			lst2.append(i)
		if len(lst1)==len(lst2):
			for i in range(len(lst1)):
				if lst1[i]!=lst2[i]:
					c+=1
		else:
			print("no")
		if c==1:
			print("yes")
		else:
			print("no")
str1,str2=map(str,input().split())
call=checkchar()
call.differby1(str1,str2)
