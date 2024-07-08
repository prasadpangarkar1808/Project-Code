rollno=[]
name=[]
marks=[]

def addstudent():
    sroll=int(input("Enter Student Roll No = "))
    sname=input("Enter Student Name = ")
    smarks=int(input("Enter Student Mark = "))
    rollno.append(sroll)
    name.append(sname)
    marks.append(smarks)

def viewstudent():
    print("Roll No \t Name \t\t Marks")
    for i in range(len(rollno)):
        print(rollno[i] , "\t\t" , name[i] , "\t" , marks[i])

def updatestudent():
    froll=int(input("Enter Roll Number to Find = "))
    for i in range(len(rollno)):
        if rollno[i]==froll:
            uroll=int(input("Enter Student Roll No = "))
            uname=input("Enter Student Name = ")
            umarks=int(input("Enter Student Mark = "))

            rollno[i]=uroll
            name[i]=uname
            marks[i]=umarks

def deletestudent():
    droll=int(input("Enter Roll Number to Delete = "))
    for i in range(len(rollno)):
        if rollno[i]==droll:
            rollno.remove(rollno[i])
            name.remove(name[i])
            marks.remove(marks[i])
            break

def searchstudent():
    ssroll=int(input("Enter Roll Number to Search = "))
    for i in range(len(rollno)):
        if rollno[i]==ssroll:
            print(rollno[i] , "\t\t" , name[i] , "\t" , marks[i])


count=3
while(count!=0):
    uname=input("Enter your username = ")
    upass=input("Enter your password = ")
    if(uname=="admin" and upass=="1234"):
        print("Login Successfully")
        print("Student Management System")
        cnt=1
        while(cnt!=0):
            print("1. Add Student \n 2. View List \n 3. Update \n 4. Search \n 5. Delete \n 6. Exit")
            ch=int(input("Enter your Choice = "))
        
            if(ch==1):
                print("Add Student")
                addstudent()
            elif(ch==2):
                print("View List")
                viewstudent()
            elif(ch==3):
                print("Update")
                updatestudent()
            elif(ch==4):
                print("Search Student")
                searchstudent()
            elif(ch==5):
                 print("Delete")
                 deletestudent()
            elif ch==6:
                    cnt=0
        count=1
    elif(uname!="admin" and upass!="1234"):
        print("Login Failed both incorrect")
    elif(uname!="admin"):
        print("Incorrect Username")
    elif(upass!="1234"):
        print("Incorrect Password")
    count-=1
    print("Remaining Attempts = ",count)