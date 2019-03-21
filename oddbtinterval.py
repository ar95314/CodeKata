class calculate:
  def oddinterval(self,start,end):
    for i in range(start+1,end):
      if(i%2!=0):
        print(i,"",end=" ")
start,end=map(int,input().split())
cal=calculate()
cal.oddinterval(start,end)
