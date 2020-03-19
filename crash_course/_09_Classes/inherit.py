class Parent():

    def __init__(self, param1, param2):

        self.p1 = param1
        self.p2 = param2
    
    def parent_print(self):
        print('%s %s' % (self.p1,self.p2))

my_obj01 = Parent('argument1', 'argument2')

my_obj01.parent_print()


class Child(Parent):
    def __init__(self, param1, param2, param3):
        super().__init__(param1, param2)

        self.p3 = param3
    

    def child_print(self):
        print('%s %s %s' % (self.p1,self.p2,self.p3))

my_obj02 = Child('argument1', 'argument2', 'argument3')

my_obj02.child_print()