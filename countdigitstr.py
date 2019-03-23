class countof:
	def digit(self,str):
		count=0
		for i in range(0,len(str)):
				if str[i].isdigit() :
					count+=1
				else:
					continue
		print(count)
str=input()
call=countof()
call.digit(str)
