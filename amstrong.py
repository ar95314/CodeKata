class checkamstrong:
  def amstrong(self,num):
    ams=r=0
    temp=num
    while num>0:
      r=num%10
      ams+=r**3
      num=num//10
    if temp==ams:
      print("yes")
    else:
      print("no")
num=int(input())
call=checkamstrong()
call.amstrong(num)
