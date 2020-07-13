import time as tts
def rep(name, val):
	f= open("report.txt","a")
	f.write("value \t" + name +" equals\t%d \t at time %d \n"%(val, tts.time()))
	f.close()

