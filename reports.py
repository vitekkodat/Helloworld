import time as tts
def nrep():
	f= open("report.txt","w+")
	f.close()
def rep(name, val):
	f= open("report.txt","a")
	f.write("value \t" + name +" equals\t%f \t at time %f \n"%(val, tts.time()))
	f.close()

