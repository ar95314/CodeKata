class calprime:
  def prime(self,start,end):
    for num in range(start+1,end):
      for i in range(2,num):
        if num%i==0:
         break
      else:
      	print(num)
start,end=map(int,input().split())
c=calprime()
c.prime(start,end)
