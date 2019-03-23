class countofsp:
	def symbol(self,str):
		count=0
		for i in range(0,len(str)):
				if str[i].isalpha():
					continue
				elif str[i].isdigit():
					continue
				elif str[i]==" ":
					continue
				else:
					count+=1
		print(count)
str=input()
call=countofsp()
call.symbol(str)
