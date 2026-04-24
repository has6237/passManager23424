def menu():
    print("Wlcome to your password manager")
    print("1. Add a password")
    print("2. View all password")
    print("3. Change a password")
    print("4. Delete password")

    menu_choise = int(input("Enter your choise: "))

    if menu_choise == 1:
        addPassword()
    elif menu_choise == 2:
        viewAll()
    elif menu_choise == 3:
        changePass()
    elif menu_choise == 4:
        deletePass()
    else:
        print("Invalid choise.")
        menu()

passwords = []

def addPassword():
    print("Add password")

    site_name = input("Enter site name: ")
    site_domain = input("Enter site domain: ")
    site_password = input("Enter site password: ")

    passwords.append({
        "site_number": len(passwords) + 1,
        "site_name": site_name,
        "site_domain": site_domain,
        "site_password": site_password
    })
    print("Site successfully added")

    menu()


def viewAll():
    print("View all password")
    for i, password in enumerate(passwords):
        print(f"{i+1}.")
        print(f"Site number: {password['site_number']}")
        print(f"Site name: {password['site_name']}")
        print(f"Site domain: {password['site_domain']}")
        print(f"Site password: {password['site_password']}")
        print("------------------------------------------")
    menu()

def changePass():
    print("Change a password")

    input_site_number = int(input("Enter site number: "))
    found = False
    for password in passwords:
        if password['site_number'] == input_site_number:
            print(f"Site number: {password['site_number']}")
            print(f"Site name: {password['site_name']}")
            print(f"Site domain: {password['site_domain']}")
            print(f"Site password: {password['site_password']}")

            new_password = input("Enter new password: ")
            password["site_password"] = new_password
            print("Password successfully changed")
            found = True
            break

        if not found:
            print("No site found")
    menu()


def deletePass():
    print("Delete a password")

    input_site_number = int(input("Enter the site number: "))
    found = False

    for password in passwords:
        if password['site_number'] == input_site_number:
            print(f"Site number: {password['site_number']}")
            print(f"Site name: {password['site_name']}")
            print(f"Site domain: {password['site_domain']}")
            print(f"Site password: {password['site_password']}")

            delete_confirmation = int(input("Press 1 to delete or 0 to back: "))

            if delete_confirmation == 1:
                passwords.remove(password)
                print("Password successfully deleted")
            elif delete_confirmation == 0:
                menu()
                return

            found = True
            break

    if not found:
        print("No site found")

    menu()
            
menu()
