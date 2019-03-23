class noofdigit:
	def number(self,n):
		count=0
		for i in range(len(n)):
			count+=1
		print(count)
n=input()
call=noofdigit()
call.number(n)
