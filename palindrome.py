class palindrome:
	def check(self,s):
		temp=""
		for i in s:
			temp=i+temp
		if temp==s:
			print("yes")
		else:
			print("no")
s=input()
call=palindrome()
call.check(s)
		
