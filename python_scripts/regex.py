import re

line = "iCats are better than Dogs"
repl = "prashant"
retobj = re.sub(r'iCats',repl,line)

if retobj:
 print ("True")
 print line 
else:
 print ("false")
