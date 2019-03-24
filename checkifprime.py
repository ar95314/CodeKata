class checkprime:
  def prime(self,n):
    for i in range(2,n):
      if n%i==0:
        print("no")
        break
    else:
      print("yes")
n=int(input())
c=checkprime()
c.prime(n)
