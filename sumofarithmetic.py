lst=[]
class arithmetic:
	def sum(self,a,d,n):
		sum=0
		dig=a
		for i in range(0,n):
			lst.append(dig)
			dig+=d
		for i in range(0,len(lst)):
			sum+=lst[i]
		print(sum)
n,a,d=map(int,input().split())
call=arithmetic()
call.sum(a,d,n)
    
