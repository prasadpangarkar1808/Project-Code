data=input("Enter tha data = ")

with open('example.txt','w')as file:
    file.write(f'{data}\n')

with open('example.txt','r')as file:
    example = file.read()

print(example) #print the file data

