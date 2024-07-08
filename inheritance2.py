class parent():
    def fun1(self):
        print("Parent fun1")

class child():
    def fun2(self):
        print("Child fun2")

class child2(parent, child):
        def fun3(self):
            print("Child fun3")
        
obj1=child2()
obj1.fun1()
obj1.fun2()
obj1.fun3()
