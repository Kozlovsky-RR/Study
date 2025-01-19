class Book:
    def __init__(self, title, author, year, genre,  pages):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    @property
    def title(self) :
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise ValueError("Название должно быть не пустой строкой")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            raise ValueError("Имя автора должно быть строкой")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and value >= 0:
            self._year = value
        else:
            raise ValueError("Год должен быть положительным числом")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if isinstance(value, str):
            self._genre = value
        else:
            raise ValueError("Жанр должен быть строкой")

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value >= 0:
            self._pages = value
        else:
            raise ValueError("Страница должна быть положительным числом")

    def __str__(self):
        return f'{self.title}, {self.author}, {self.year}, {self.genre}, {self.pages}'

    def __repr__(self):
        return f'Book({self.title}), Book({self.author}), Book({self.year}), Book({self.genre}), Book({self.pages})'


class Library:

    def __init__(self):
        self.bookshelf = []

    def add_book(self, book) :
        self.bookshelf.append(book)

    def search_by_title(self, title):
        for i in self.bookshelf:
            if i.title == title:
                return i
        return "Книга отсутствует в библиотеке"

    def get_books_by_author(self, author):
        return [i for i in self.bookshelf if i.author == author]

    def get_books_sorted_by_year(self):
        return sorted(self.bookshelf, key=lambda x: x.year)

    def remove_book(self, book):
        list(self.bookshelf).remove(book)


library = Library()
book1 = Book("Title1", "Author1", 2001, "Genre1", 300)
book2 = Book("Title2", "Author2", 1999, "Genre2", 150)
book3 = Book("Title3", "Author1", 2010, "Genre3", 400)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.search_by_title("Title1"))
print(library.get_books_by_author("Author1"))
print(library.get_books_sorted_by_year())
