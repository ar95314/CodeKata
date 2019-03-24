class ifoddeve:
	def sub(self,n,m):
		s=n-m
		s=abs(s)
		if s%2==0:
			print("even")
		else:
			print("odd")
n,m=map(int,input().split())
call=ifoddeve()
call.sub(n,m)
