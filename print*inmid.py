lst=[]
class changeto:
	def midle(self,s):
		for i in s:
			lst.append(i)
		if len(s)%2==0:
			leng=int(len(s)/2)
			lst[leng]='*'
			lst[leng-1]='*'
		else:
			leng=int((len(s))/2)
			lst[leng]='*'
		for i in range(0,len(lst)):
			if i==((len(lst))-1):
				print(lst[i])
			else:
				print(lst[i],end=" ")
s=input()
call=changeto()
call.midle(s)
