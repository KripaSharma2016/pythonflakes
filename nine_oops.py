'''
Created on Jan 26, 2017

@author: kripa
'''

class C:
    def printer(self,name = None,age = None):
        self.name =name
        if self.name == None:
            print("this is first")
        else:
            print(self.name)    
    '''def printer(self,name):   
        self.name=name
        print(self.name) '''

c1 =C()
c1.printer()
c2 = C()
c2.printer('jerin')                           