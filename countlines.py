class countof:
	def line(self,str):
		count=0
		for i in range(0,len(str)):
				if str[i]=="." :
					count+=1
				else:
					continue
		count+=1
		print(count)
str=input()
call=countof()
call.line(str)
