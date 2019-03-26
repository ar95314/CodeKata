class simplecalc:
	def divmod(self,n1,op,n2):
		if op=='/':
			n=int(n1)/int(n2)
			print(int(n))
		else:
			n=int(n1)%int(n2)
			print(int(n))
n1,op,n2=map(str,input().split())
call=simplecalc()
call.divmod(n1,op,n2)
