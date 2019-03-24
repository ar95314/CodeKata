class numbertoword:
	def printinword(self,n):
		lst=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
		leng=len(lst)
		for i in range(1,leng+1):
			if i==n:
				print(lst[i-1])
n=int(input())
call=numbertoword()
call.printinword(n)
