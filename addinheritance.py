class num1:
    def add1(self):
        self.num = int(input("Enter num1 = "))

class num2(num1):
    def add2(self):
        self.num2 = int(input("Enter num2 = "))
        print("Addition = ", self.num + self.num2)

obj = num2()
obj.add1()
obj.add2()
