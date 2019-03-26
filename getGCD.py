class gcd:
	def checkit(self,n,m):
		if n > m:
			smaller = m
		else:
			smaller = n
		for i in range(1, smaller+1):
			if((n % i == 0) and (m % i == 0)):
				hcf = i
		print(hcf)
n,m=map(int,input().split())
call=gcd()
call.checkit(n,m)
        
