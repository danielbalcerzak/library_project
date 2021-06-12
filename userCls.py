class User:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.books = []

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"User has {len(self.books)}: {[book.title for book in self.books]}")
