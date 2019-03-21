class calpower:
  def pwr(self,num,k):
    val=num**k
    return val
num,k=map(int,input().split())
c=calpower()
print(c.pwr(num,k))
