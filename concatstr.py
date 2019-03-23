class concatstr:
	def concat(self,str1,str2):
		str=str1+str2
		print(str)
str1,str2=map(str,input().split())
call=concatstr()
call.concat(str1,str2)
