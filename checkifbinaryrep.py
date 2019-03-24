class checkbinary:
	def find(self,s):
		c=0
		lst=['0','1']
		for i in s:
			if i not in lst:
				c=1
				break
		if c==1:
			print("no")
		else:
			print("yes")
s=input()
call=checkbinary()
call.find(s)
