def rep(name, val):
	f= open("report.txt","w+")
	f.write("value \t" + name +" equals\t%d\n"%val)
	f.close()

