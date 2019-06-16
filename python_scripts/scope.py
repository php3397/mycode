#module demo for filehandling
import sys
def fh(filename):
	with open('filename','w+') as fh:
		fh.write("this is a newfile called filename \n")
		fh.close()

ob1=fh('samplefile.tt')





