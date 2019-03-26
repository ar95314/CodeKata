lst1=[]
lst2=[]
class printstr:
	def inoddeve(self,s):
		for i in range(len(s)):
			if i%2==0:
				lst1.append(s[i])
			else:
				lst2.append(s[i])
		for i in range(len(lst1)):
			print(lst1[i],end="")
		print(end=" ")
		for i in range(len(lst2)):
			if i==(len(lst2)-1):
				print(lst2[i])
			else:
				print(lst2[i],end="")
s=input()
call=printstr()
call.inoddeve(s)
