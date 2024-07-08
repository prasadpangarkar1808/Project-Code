import csv

roll=input("Enter The roll = ")
name=input("Enter the name = ")
marks=input("Enter the marks = ")

stud_details=[roll, name, marks]

with open('studnent.csv','a',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(stud_details)

with open('studnent.csv','r')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)