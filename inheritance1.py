class parent():
    def fun1(self):
        print("Parent fun1")
    
class child(parent):
    def fun2(self):
        print("Child fun2")

obj1=child()
obj1.fun1()
obj1.fun2()