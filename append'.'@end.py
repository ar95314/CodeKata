string=input()
lst=[]
n=len(string)
for i in string:
	lst.append(i)
for i in range(len(lst)):
	if i==len(lst)-1:
		lst.append('.')
for i in range(len(lst)):
	if i == len(lst)-1:
		print(lst[i])
	else:
		print(lst[i],end="")
