lst=[]
class checkamstrong:
    def amstrong(self,start,end):
        for num in range(start+1,end):
            ams=r=temp=0
            temp=num
            while num>0:
                r=num%10
                ams+=r**3
                num=num//10
            if temp==ams:
                lst.append(temp)
        for i in range(0,len(lst)):
            if i==(len(lst)-1):
                print(lst[i])
            else:
                print(lst[i],end=" ")
start,end=map(int,input().split())
call=checkamstrong()
call.amstrong(start,end)
