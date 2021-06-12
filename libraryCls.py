import bookCls
import userCls


class Library:

    def __init__(self):
        self.users = []
        self.books = []

    "BOOKS METHODS ARE HERE"

    def add_new_book(self, author: str, title: str):
        new_book = bookCls.Book(author, title)
        self.books.append(new_book)

    def delete_book(self, author: str, title: str):
        for i in self.books:
            if i.title == title and i.author == author:
                self.books.remove(i)

    def return_books(self) -> list:
        return self.books

    def return_available_books(self) -> list:
        available = []
        for i in self.books:
            if not i.is_rent():
                available.append(i)
        return available

    def if_available(self, title) -> bool:
        for book in self.books:
            if book.title == title:
                return book.is_rent()

    def return_rents_books(self) -> list:
        rents = []
        for i in self.books:
            if i.is_rent():
                rents.append(i)
        return rents

    def show_book_info(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Author: {book.author}")
                print(f"Title: {book.title}")
                print(f"Num of rent: {book.show_how_many_rents()}")
                print(f"If rent: {book.is_rent()}")
                print(f"Rent by: "
                      f"{(book.rent_by[0].name + ' ' + book.rent_by[0].surname) if book.is_rent() is True else None}")
            else:
                print(f"There is no book with title: {title}")

    "USERS METHODS ARE HERE"

    def add_user(self, name: str, surname: str):
        new_user = userCls.User(name, surname)
        self.users.append(new_user)
        print("User was added")

    def del_user(self, name: str, surname: str):
        for user in self.users:
            if user.name == name and user.surname == surname:
                print(f"{user.name} {user.surname} was removed successful")
                self.users.remove(user)
            else:
                print("There is no user in library")

    def show_users(self):
        users = []
        for user in self.users:
            users.append(f"{user.name} {user.surname}")
        return users

    def show_user_info(self, name, surname):
        for user in self.users:
            if user.name == name and user.surname == surname:
                user.show_info()
            else:
                print(f"There is no {name} {surname} in base")

    "METHODS TO RENT AND RETURN BOOK"

    def rent_a_book(self, author: str, title: str, userName, userSurname):
        for book in self.books:
            if book.author == author and book.title == title:
                if book in self.return_available_books():
                    for user in self.users:
                        if user.name == userName and user.surname == userSurname:
                            user.books.append(book)
                            book.rent_by.append(user)
                            book.change_status()
                            book.add_num_of_rent()
                            print(f"{user.name} {user.surname} has rent {book.author} {book.title}")
                        else:
                            print("There's no user in library")
                elif book in self.return_rents_books():
                    print("The book is already rent by another user")
            else:
                print(f"The book {author} {title} isn't in library")

    def return_a_book(self, author: str, title: str):
        for book in self.books:
            if book.author == author and book.title == title:
                if book in self.return_rents_books():
                    print(f"The book {book.title} {book.author} is return from "
                          f"{book.rent_by[0].name} {book.rent_by[0].surname}")
                    book.rent_by[0].books.remove(book)
                    book.rent_by.clear()
                    book.change_status()
                else:
                    print(f"The book {book.author} {book.title} isn't rent")
            else:
                print(f"The book {author} {title} isn't in library")
