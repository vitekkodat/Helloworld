def rep(name, val):
	f= open("report.txt","w+")
	f.write("value \t" + name +"\t %d" %val)
	f.close()

