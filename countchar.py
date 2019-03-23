class count:
	def string(self,str):
		ch=0
		for i in range(len(str)):
			if str[i]==" ":
				continue
			else:
				ch+=1
		print(ch)
str=input()
call=count()
call.string(str)
