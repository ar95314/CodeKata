lst1=[]
class findno:
	def appearonce(self,n,lst):
		lst.sort()
		for i in range(0,n):
			if i!=n-1:
				if lst[i]==lst[i+1]:
					if lst[i] not in lst1:
						lst1.append(lst[i])
		for i in range(len(lst)):
			if lst[i] not in lst1:
				print(lst[i])
n=int(input())
lst=list(map(int,input().split()))
call=findno()
call.appearonce(n,lst)
