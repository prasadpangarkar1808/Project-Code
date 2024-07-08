#Pass@123
password=input("Enter Password = ")
lcnt=0
ucnt=0
dcnt=0
scnt=0
for i in range(len(password)):
    if(password[i]>='a' and password[i]<='z'):
        lcnt+=1
    elif(password[i]>='A' and password[i]<='Z'):
        ucnt+=1
    elif(password[i]>'0' and password[i]<='9'):
        dcnt+=1
    else:
        scnt+=1

if(lcnt!=0 and ucnt!=0 and dcnt!=0 and scnt!=0 and len(password)>=0):
    print("Valid Password")
else:
    print("Invalid Password")