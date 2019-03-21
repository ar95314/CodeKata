lst=[]
class multiply:
  def fivemul(self,n):
    for i in range(1,6):
      lst=i*n
      print(lst,end=" ")
n=int(input())
call=multiply()
call.fivemul(n)
