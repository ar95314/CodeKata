lst=[]
class printstr:
	def forktime(self,s,k):
		a=int(k)
		for i in range(a):
			lst.append(s[i])
		for i in range(len(lst)):
			if i==(len(lst)-1):
				print(lst[i])
			else:
				print(lst[i],end="")
s,k=map(str,input().split())
call=printstr()
call.forktime(s,k)
