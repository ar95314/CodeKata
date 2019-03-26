class area:
	def round5(self,leng,bred):
		area=leng*bred
		print("{:.5f}".format(area))
leng,bred=map(float,input().split())
call=area()
call.round5(leng,bred)
