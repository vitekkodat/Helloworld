import time as tts
def nrep():
	f= open("report.txt","w+")
	f.close()
def rep(name, val):
	f= open("report.txt","a")
	f.write("value \t" + name +" equals\t%d \t at time %d \n"%(val, tts.time()))
	f.close()

