def rep(name, val):
	f= open("report.txt","w+")
	f.write("value \t" + name +" equals to \t %d" %val)
	f.close()

