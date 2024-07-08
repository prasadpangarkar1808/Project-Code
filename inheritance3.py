class parent():
    def fun1(self):
        print("Parent fun1")

class child(parent):
    def fun2(self):
        print("Child fun2")

class child2(child):
    def fun3(self):
        print("Child fun3")

obj=child2()
obj.fun1()
obj.fun2()
obj.fun3()