def rep(name, val):
	f= open("report.txt","w+")
	f.write("value \t" + name +" equals\t")
	f.write(val)
	f.write("\n")
	f.close()

