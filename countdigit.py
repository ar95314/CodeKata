class count:
  def digit(self,n):
    count=0
    while n>0:
      n=n//10
      count+=1
    print(count)
n=int(input())
call=count()
call.digit(n)
