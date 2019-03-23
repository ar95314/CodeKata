class countof:
	def spaces(self,str):
		count=0
		for i in range(0,len(str)):
				if str[i]==" " :
					count+=1
				else:
					continue
		print(count)
str=input()
call=countof()
call.spaces(str)
