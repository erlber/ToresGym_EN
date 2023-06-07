import time
import datetime

def space(num):
    for _ in range(num):
        print("")

members = [[101, "Finn Olav", "Konan", "2023-05-01", True], [102, "Magnar", "Rabliås", "2022-09-12", False], [103, "Arne-Jhonny", "Benz", "2023-01-31", True]]
# index    | 0  |      1     |    2   |      3      |  4  |
# 0 = ID
# 1 = First Name
# 2 = Last Name
# 3 = Registration Date
# 4 = Active Membership True/False

def mainMenu():
    print("|---- Membership Register for Tore's Gym ----|")
    print("|                                           |")
    print("|-----------------|MENU|--------------------|")
    print("| 1. Add new member                          |")
    print("| 2. Edit member                              |")
    print("| 3. Delete member                            |")
    print("| 4. List all members                         |")
    print("| 5. Search for a member                       |")
    print("| 0. Exit program                             |")
    print("|---------------------------------------------|")
    choice = input("  Choose a number from the menu: ")
    return choice

def addMember():
    space(50)
    print("|----------- Add new member ------------|")
    print("|                                      |")
    firstName = input("| First Name: ")
    lastName = input("| Last Name: ")
    regDate = str(datetime.date.today())
    active = input("| Activate membership? y/n: ")
    if active == "y":
        active = True
    else:
        active = False
    
    id = 0
    for member in members:
        if id < member[0]:
            id = member[0] + 1
    
    newMember = [id, firstName, lastName, regDate, active]
    members.append(newMember)

    listMembers(2, [newMember])
    print("| Successfully registered in Tore's Gym")
    input("| Press any key to go back to the main menu: ")

    return ""

def listMembers(version, membersList=members):
    space(2)
    if version == 1:
        for member in membersList:
            print(f"| ID: {member[0]}")
            time.sleep(0.2)
            print(f"| First Name: {member[1]}")
            time.sleep(0.2)
            print(f"| Last Name: {member[2]}")
            time.sleep(0.2)
            print(f"| Registered: {member[3]}")
            time.sleep(0.2)
            if member[4]:
                print("| Membership: Active")
            else:
                print("| Membership: Deactivated")
            space(1)
            time.sleep(0.5)
        space(1)
        input("Press any key to go back to the main menu: ")

    elif version == 2:
        for member in membersList:
            print(f"| ID: {member[0]} Name: {member[1]} {member[2]}")
            time.sleep(0.2)
    
    return ""

def editMember():
    space(50)
    while True:
        print("|-----------|Edit member|-----------|")
        print("|                                    |")
        print("| 1. Enter ID to edit a member       |")
        print("| 2. List all members with IDs       |")
        print("| 0. Back to main menu               |")
        print("|------------------------------------|")
        choice = input("  Choose a number from the menu: ")
        space(1)

        if choice == "1":
            id = input("   Enter the ID of the member: ")
            for member in members:
                if member[0] == int(id):

                    firstName = input("Enter the new first name or press enter to skip: ")
                    if firstName:
                        member[1] = firstName

                    lastName = input("Enter the new last name or press enter to skip: ")
                    if lastName:
                        member[2] = lastName
                    
                    while True:
                        active = input("Set membership to active y/n or press enter to skip: ")
                        if active == "y":
                            member[4] = True
                            break
                        elif active == "n":
                            member[4] = False
                            break
                        elif not active:
                            break
                        else:
                            print("Invalid input value, choose 'y' or 'n'")
                            space(1)

        elif choice == "2":
            listMembers(2)
        
        elif choice == "0":
            break

    return ""

def deleteMember():
    space(50)
    while True:
        print("|---------|Delete member|----------|")
        print("|                                    |")
        print("| 1. Delete member                   |")
        print("| 2. List all members with IDs       |")
        print("| 0. Back to main menu               |")
        print("|------------------------------------|")
        choice = input("  Choose a number from the menu: ")
        space(1)

        if choice == "1":
            id = input(" Enter the ID of the member you want to delete: ")
            counter = 0
            for member in members:
                if member[0] == int(id):
                    members.pop(counter)
                counter  += 1

        elif choice == "2":
            listMembers(2)
        elif choice == "0":
            break

    return ""

def searchMember():
    searchList = []
    name = input("  Name of the member you want to search for: ").lower()
    for member in members:
        if name in member[1].lower() or name in member[2].lower():
            searchList.append(member)
    
    listMembers(1, searchList)

def main():
    run = True
    choice = ""
    while run:
        if choice == "0":
            break
        
        elif choice == "1":
            choice = addMember()

        elif choice == "2":
            choice = editMember()

        elif choice == "3":
            choice = deleteMember()

        elif choice == "4":
            choice = listMembers(1)

        elif choice == "5":
            choice = searchMember()

        else:
            choice = mainMenu()
    
main()
