lst1=[]
class findrepeat:
	def inlist(self,n,lst):
		lst.sort()
		for i in range(0,n):
			if i!=n-1:
				if lst[i]==lst[i+1]:
					if lst[i] not in lst1:
						lst1.append(lst[i])
		for i in range(len(lst1)):
			if i==len(lst1)-1:
				print(lst1[i])
			else:
				print(lst1[i],end=" ")
n=int(input())
lst=list(map(int,input().split()))
call=findrepeat()
call.inlist(n,lst)
