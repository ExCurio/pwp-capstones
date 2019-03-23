# ********************
# Tome Rater!!!
# ********************


# ********************
# Define the User class
# ********************
class User(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "{name}'s email address has been updated.".format(name = self.name)

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name = self.name, email = self.email, books = self.books)

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        n = 0
        if len(self.books) > 0:
            for rating in self.books.values():
                if rating:
                    total += rating
                    n += 1
                else:
                    continue
        if n > 0:
            return total/n
        else:
            print("There are no books with ratings for {user}".format(user=self.name))

    def get_books_read(self):
        return len(self.books)


# ********************
# Define the Book class
# ********************

class Book:

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "{title}'s ISBN has been updated".format(title = self.title)

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.rating.append(rating)
        else:
            return "Invalid Rating"

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        average = 0
        for ratings in self.rating:
            average += ratings / len(self.rating)
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))


# ********************
# Define the Fiction class
# ********************

class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)


# ********************
# Define the Non-Fiction class
# ********************

class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title} a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


# ********************
# Define TomeRater class
# ********************

class TomeRater:

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if self.users.get(email):
            self.users[email].read_book(book, rating)
            self.books[book] = self.books.get(book, 0) + 1
            if rating:
                    book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email = email))

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    

    # ********************
    # Analysis Methods
    # ********************

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_reading = 0
        most_book = ""
        for book, read in self.books.items():
            if read > most_reading:
                most_book = book
                most_reading = read
            else:
                continue
        return most_book

    def highest_rated_book(self):
        max_rating = 0
        max_book = ""
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > max_rating:
                max_book = book
                max_rating = rating
            else:
                continue
        return max_book

    def most_positive_user(self):
        max_rating = 0
        max_user = ""
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > max_rating:
                max_user = user
                max_rating = rating
            else:
                continue
        return max_user



    # ********************
    # Get Creative Section
    # ********************

    def get_n_most_read_books(self, n):
        if type(n) == int:
            books_sorted = [k for k in sorted(self.books, key=self.books.get, reverse=True)]
            return books_sorted[:n]
        else:
            print("The argument n = {n} is not of type int. Please pass an int.".format(n=n))

    def get_n_most_prolific_readers(self, n):
        if type(n) == int:
            readers = [(reader, reader.get_books_read()) for reader in self.users.values()]
            readers_sorted = [k[0] for k in sorted(readers, key=lambda reader: reader[1], reverse=True)]
            return readers_sorted[:n]
        else:
            print("The argument n = {n} is not of type integer. Please enter an integer.".format(n=n))    

































