class parent():
    def fun1(self):
        print("parent fun1")

class child1(parent):
    def fun2(self):
        print("child fun1")

class child2(parent):
    def fun3(self):
        print("child fun2")

class child3(parent):
    def fun4(self):
        print("child fun3")

obj=child1()
obj1=child2()
obj2=child3()
obj.fun1()
obj.fun2()
obj1.fun3()
obj2.fun4()
