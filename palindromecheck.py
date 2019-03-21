class check:
  def palindrome(self,num):
    r=0
    temp=num
    while num>0:
      dig=num%10
      r=r*10+dig
      num=num//10
    if r==temp:
      print("yes")
    else:
      print("no")
num=int(input())
c=check()
c.palindrome(num)
      
