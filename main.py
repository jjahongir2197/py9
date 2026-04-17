phonebook = {}

while True:
    print("1 Add")
    print("2 Search")
    print("3 Show")
    print("4 Exit")

    ch = input("Choose: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        phonebook[name] = phone

    elif ch == "2":
        name = input("Name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("Not found")

    elif ch == "3":
        for n in phonebook:
            print(n, ":", phonebook[n])

    elif ch == "4":
        break
