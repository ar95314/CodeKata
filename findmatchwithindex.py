lst1=[]
class findmatch:
	def withindex(self,n,lst):
		for i in range(n):
			if i==lst[i]:
				lst1.append(i)
		if len(lst1)==0:
			print(-1)
		else:
			for i in range(len(lst1)):
				if i==len(lst1)-1:
					print(lst1[i])
				else:
					print(lst1[i],end=" ")
n=int(input())
lst=list(map(int,input().split()))
call=findmatch()
call.withindex(n,lst)
