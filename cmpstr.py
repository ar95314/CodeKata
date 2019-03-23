class cmpstr:
	def compare(self,str1,str2):
		if len(str1)>=len(str2):
			print(str1)
		elif len(str1)<=len(str2):
			print(str2)
		else:
			print(str1)
str1,str2=map(str,input().split())
call=cmpstr()
call.compare(str1,str2)
