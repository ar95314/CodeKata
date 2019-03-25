class ifvowel:
	def check(self,s):
		flag=0
		lst=['a','A','e','E','i','I','o','O','u','U']
		for i in s:
			if i in lst:
				flag=1
		if flag==1:
			print("yes")
		else:
			print("no")
s=input()
call=ifvowel()
call.check(s)
