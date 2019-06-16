class parent:
    def __init__(self):
        print "inside parent class"

    def parentmethod(self):
        print "calling parent method"

class child(parent):
    def __init__(self):
        print "inside child class"

    def childmethod(self):
        print "calling child method"

c=child()
p=parent()

c.childmethod()
p.parentmethod()
c.parentmethod()

