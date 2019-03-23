class swapbitwise:
	def usexor(self,fst,sec):
		fst=fst^sec
		sec=fst^sec
		fst=fst^sec
		print(fst,sec)
fst,sec=map(int,input().split())
call=swapbitwise()
call.usexor(fst,sec)
