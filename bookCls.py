class Book:

    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.rent_by = []
        self.__is_rent = False
        self.__num_of_rent = 0

    def change_status(self):
        self.__is_rent = not self.__is_rent

    def is_rent(self):
        return self.__is_rent

    def show_how_many_rents(self):
        return self.__num_of_rent

    def add_num_of_rent(self):
        self.__num_of_rent += 1
