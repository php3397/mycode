fh1=open("test.txt","r+")
fh2=open("test2.txt","r+")

#read data
l=[]
line1=fh1.readline()
line2=fh2.readline()
print(line1,line2)
fh3=open("test3.txt","r+")
print(line1)
print(line2)
line="line1"+"line2"
fh3.write(line)
print(fh3.readline())

fh1.close()
fh2.close()
fh3.close()
