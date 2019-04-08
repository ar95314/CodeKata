val=0
dic={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}
lst=[]
rom=input()
rom=rom.upper()
if rom in dic:
	print(dic[rom])
else:
	for i in rom:
		lst.append(i)
	for i in lst:
		if i in dic:
			val+=dic[i]
	print(val)
