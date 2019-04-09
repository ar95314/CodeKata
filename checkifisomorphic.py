lst1=[]
lst2=[]
class check:
	def ifisomorphic(self,n,m):
		for i in n:
			lst1.append(i)
		for i in m:
			lst2.append(i)
		len1=len(set(lst1))
		len2=len(set(lst2))
		if len1==len2:
			print("yes")
		else:
			print("no")
n,m=map(str,input().split())
call=check()
call.ifisomorphic(n,m)
			
