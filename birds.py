def addbirds():
    bid = input("Enter the login id: ")
    bdays = input("Enter the days: ")
    blocation = input("Enter the location: ")
    bspecies = input("Enter the species: ")
    
    id.append(bid)
    days.append(bdays)
    location.append(blocation)
    species.append(bspecies)
    
    global session_bird_count  # Count birds added in this session
    session_bird_count += 1

def viewbirds():
    print("id \t days \t location \t species")
    for i in range(len(id)):
        print(id[i], "\t", days[i], "\t", location[i], "\t", species[i]) 

def updatebirds():
    fid = input("Enter find id: ")
    for i in range(len(id)):
        if id[i] == fid:
            ubid = input("Enter the id no: ")
            ubdays = input("Enter the days: ")
            ublocation = input("Enter the location: ")
            ubspecies = input("Enter the species: ")
            id[i] = ubid
            days[i] = ubdays
            location[i] = ublocation
            species[i] = ubspecies

def deletebirds():
    did = input("Enter the delete id: ")
    for i in range(len(id)):
        if id[i] == did:
            id.pop(i)
            days.pop(i)
            location.pop(i)
            species.pop(i)
            break

def countbirds():
    print("Birds added in this session:", session_bird_count)

def reportbirds():
    rloc = input("Enter the location for sighting: ")
    print("id \t days \t location \t species")
    for i in range(len(id)):
        if location[i] == rloc:
            print(id[i], "\t", days[i], "\t", location[i], "\t", species[i]) 

def averagebirds():
    l = []
    for i in range(len(id)):
        ele = int(input("Enter the element: "))
        l.append(ele)
    print(l)
    addition = sum(l)
    print(addition)
    average = addition / len(id)
    print("average", average)

id = []
days = []
location = []
species = []
session_bird_count = 0  # Counter for birds added in this session

count = 3
while count != 0:
    uname = input("Enter the username: ")
    upass = input("Enter the password: ")
    if uname == "admin" and upass == "1234":
        print("Login successful")
        count = 1
        cnt = 1
        while cnt != 0:
            print("Bird Watching Log")
            print("1. Add Birds")
            print("2. View list")
            print("3. Update")
            print("4. Delete")
            print("5. Count")
            print("6. Report")
            print("7. Average")
            print("8. Exit")
            ch = int(input("Enter the choice: "))

            if ch == 1:
                print("Add Birds")
                addbirds()
            if ch == 2:
                print("View birds")
                viewbirds()
            if ch == 3:
                print("Update birds")
                updatebirds()
            if ch == 4:
                print("Delete birds")
                deletebirds()
            if ch == 5:
                print("Count birds")
                countbirds()
            if ch == 6:
                print("Report birds")
                reportbirds()
            if ch == 7:
                print("Average birds")
                averagebirds()
            if ch == 8:
                print("Exiting program")
                exit()
                cnt = 0
                
    else:
        if uname != "admin" and upass != "1234":
            print("Username and password incorrect")
        elif uname != "admin":
            print("Username incorrect")
        elif upass != "1234":
            print("Password incorrect")
        
        count -= 1
        print("Remaining attempts", count)
