lst1=[]
class printno:
	def findKodd(sef,n,k,lst):
		for i in range(len(lst)):
			if lst[i]%2!=0:
				lst1.append(lst[i])
		for i in range(len(lst1)):
			if i==k-1:
				print(lst1[i])
n,k=map(int,input().split())
lst=list(map(int,input().split()))
call=printno()
call.findKodd(n,k,lst)
