class swap:
	def number(self,fst,sec):
		fst=fst+sec
		sec=fst-sec
		fst=fst-sec
		print(fst,sec)
fst,sec=map(int,input().split())
call=swap()
call.number(fst,sec)
