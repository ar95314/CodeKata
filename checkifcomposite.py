class checkcomposite:
  def notprime(self,m):
    for i in range(2,m):
      if m%i==0:
        print("yes")
        break
    else:
      print("no")
m=int(input())
c=checkcomposite()
c.notprime(n)
