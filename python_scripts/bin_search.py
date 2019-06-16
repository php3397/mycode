#binary search algo

alist=[3,12212,10,2,31]

class sortme():
	def __init__(self,classlist):
		self.classlist=classlist
	
	def sort(self):
		print ("I will sort you here, first digit is %d",self.classlist[0])
			max=0
			for i in range(0,len(self.classlist)-1):
				if self.classlist[i] > max:
					max=self.classlist[i]
				else:
					max=self.classlist[i+1]
			print ("max value in list is",max)
		print ("list so far is ",self.classlist)


	def easyway(self):
		return sorted(self.classlist)

sortobj = sortme(alist)
#sortedlist = sortobj.easyway()
sortedlist = sortobj.sort()
#print (sortedlist)
