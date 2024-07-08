string=input("Enter String = ")
str1=[]
print("String = ",string)
lcnt=0
for i in range(len(string)):
    if(string[i]=='a'):
        str1.append('A')
    if(string[i]=='b'):
        str1.append('B')
    if(string[i]=='c'):
        str1.append('C')
    if(string[i]=='d'):
        str1.append('D')
print(str1)