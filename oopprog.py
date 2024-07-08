#class student:
#    def putdata():
#        print("Sub main block")
#
#print("Main block")
#s1=student
#s1.putdata()

class employee:
    def getdata(self,name):
        self.name=name
    def putdata(self):
        print(f"Name = {self.name} ")

print("Emp details")
e=employee
e.getdata()
e.putdata()