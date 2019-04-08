class factorial:
  def fact(self,num):
    f=1
    for i in range(1,num+1):
      f=f*i
    print(f)
num=int(input())
call=factorial()
call.fact(num)
