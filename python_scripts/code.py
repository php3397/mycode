def extendlist(val,list=[]):
	list.append(val)
	return list

list1=extendlist(10)
list2=extendlist(123,[])
list3 = extendlist('a')

print ("list 1 = %s", list1)
print ("list 2 = %s", list2)
print ("list 3 = %s", list3)
