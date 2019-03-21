class calculate:
  def eveinterval(self,start,end):
    for i in range(start+1,end):
      if(i%2==0):
        if i==(end-1):
          print(end)
          print(i)
        else:
          print(i,end=" ")
start,end=map(int,input().split())
cal=calculate()
cal.eveinterval(start,end)
