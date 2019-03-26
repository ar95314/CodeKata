lst2=[]
class printindex:
	def ofchangeno(self,n,lst):
		for i in range(len(lst)):
			lst2.append(lst[i])
		lst.sort()
		for i in range(len(lst)):
			if lst[i]!=lst2[i]:
				print(i)
				break
n=int(input())
lst=list(map(int,input().split()))
call=printindex()
call.ofchangeno(n,lst)
