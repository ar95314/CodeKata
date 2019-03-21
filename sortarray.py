n=int(input())
lst=list(map(int,input().split()))
lst.sort()
for i in range(0,n):
	if lst[i]==lst[(n-1)]:
		print(lst[i])
	else:
		print(lst[i],end=" ")
