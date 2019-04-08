class fact:
  def factorial(self,num):
    f=1
    for i in range(1,num+1):
      f=f*i
    print(f)
num=int(input())
call=fact()
call.factorial(num)
