def menu(library):
    while True:
        print("___________MENU___________")
        print("1. USERS")
        print("2. BOOKS")
        print("3. OPERATIONS")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("__________________________")
            print("1. ADD USER")
            print("2. DELETE USER")
            print("3. SHOW USERS")
            print("4. USER INFO")
            print("5. BACK")
            action = int(input("Enter your choice: "))
            print("__________________________")
            user_actions(action, library)
        elif choice == 2:
            print("__________________________")
            print("1. ADD BOOK")
            print("2. DELETE BOOK")
            print("3. SEARCH A BOOK")
            print("4. BACK")
            action = int(input("Enter your choice: "))
            print("__________________________")
            book_actions(action, library)
        elif choice == 3:
            print("__________________________")
            print("1. RENT BOOK")
            print("2. RETURN BOOK")
            print("3. BACK")
            action = int(input("Enter your choice: "))
            print("__________________________")
            actions(action, library)


def user_actions(action, library):
    if action == 1:
        name = input("Enter name of a new user: ")
        surname = input("Enter surname of a new user: ")
        library.add_user(name, surname)
    elif action == 2:
        name = input("Enter name of a user: ")
        surname = input("Enter surname of a user: ")
        library.del_user(name, surname)
    elif action == 3:
        print(library.show_users())
    elif action == 4:
        name = input("Enter name of a user: ")
        surname = input("Enter surname of a user: ")
        library.show_user_info(name, surname)
    elif action == 5:
        menu(library)
    else:
        print("Wrong choice")
        menu(library)


def book_actions(action, library):
    if action == 1:
        author = input("Enter the author of a new book: ")
        title = input("Enter title of a new book: ")
        library.add_new_book(author, title)
    elif action == 2:
        author = input("Enter the author of a new book: ")
        title = input("Enter title of a new book: ")
        library.delete_book(author, title)
    elif action == 3:
        title = input("Enter title of a book: ")
        library.show_book_info(title)
    elif action == 4:
        menu(library)
    else:
        print("Wrong choice")
        menu(library)


def actions(action, library):
    if action == 1:
        user_name = input("Enter name of a user: ")
        surname_user = input("Enter surname of a user: ")
        author = input("Enter author of a book: ")
        title = input("Enter title of a book: ")
        library.rent_a_book(author, title, user_name, surname_user)
    elif action == 2:
        author = input("Enter author of a book: ")
        title = input("Enter title of a book: ")
        library.return_a_book(author, title)
    elif action == 3:
        menu(library)
    else:
        print("Wrong choice")
        menu(library)
