lst1=[]
class printno:
	def findKsmall(sef,n,k,lst):
		lst.sort()
		for i in range(len(lst)):
			if i==k-1:
				print(lst[i])
n,k=map(int,input().split())
lst=list(map(int,input().split()))
call=printno()
call.findKsmall(n,k,lst)
