contacts = {}
while True:
    choice = input("Hello, welcome to contact book, would you like to add/view/search/handle/delete your contacts?:")
    if choice == "add":
        user = input("enter the name of the contact: ")
        number = int(input("enter the phone number: "))
        contacts[user] = number
        print("contact saved.")
    if not contacts:
        print("No contacts saved.")
    elif choice == "view":
        print(contacts)
    elif choice == "delete":
        del_user = input("enter the contact you want to delete: ")
        if del_user in contacts:
            del contacts[del_user]
            print("contact deleted.")
        else:
            print("invalid contact")
    elif choice == "search":
        search_user = input("enter the name of the contact you want to search: ")
        if search_user in contacts:
            print("valid contact")
        else:
            print("invalid contact")
    elif choice == "quit":
        break
    else:
        print("invalid choice")

    
