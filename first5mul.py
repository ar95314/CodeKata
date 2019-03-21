lst=[]
class multiply:
  def fivemul(self,n):
    for i in range(1,6):
      lst.append(i*n)
    for i in range(0,len(lst)):
    	print(lst[i],end=" ")
n=int(input())
call=multiply()
call.fivemul(n)
