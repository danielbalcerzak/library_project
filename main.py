import func
import libraryCls


def main():
    # Adding some data to projects and function it
    library = libraryCls.Library()
    library.add_user("Joe", "Snow")
    library.add_new_book("Vonnegut", "Nr 5")
    library.rent_a_book("Vonnegut", "Nr 5", "Joe", "Snow")
    library.show_user_info("Joe", "Snow")
    library.show_book_info("Nr 5")

    # Start menu function
    func.menu(library)


if __name__ == '__main__':
    main()
