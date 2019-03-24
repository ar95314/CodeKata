class check:
	def ifalphanum(self,s):
		flag1=flag2=0
		for i in s:
			if i.isalpha():
				flag1=1
			if i.isdigit():
				flag2=1
		if flag1==1 and flag2==1:
			print("Yes")
		else:
			print("No")
s=input()
call=check()
call.ifalphanum(s)
