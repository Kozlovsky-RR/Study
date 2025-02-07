"""Библиотека для управления коллекцией книг."""


from typing import Union

class Book:
    """Класс для создания книги."""
    def __init__(self, title: str, author: str, year: int, genre: str,  pages: int) -> None:
        """Инициализация данных о книге."""
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.genre: str = genre
        self.pages: int = pages

    @property
    def title(self) -> str:
        """Геттер для названия книги."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Сеттер для названия книги."""
        if Book.checking_the_string(value, error="Название должно быть не пустой строкой"):
            self._title: str = value

    @property
    def author(self) -> str:
        """Геттер для автора книги."""
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        """Сеттер для автора книги."""
        if Book.checking_the_string(value, error="Имя автора должно быть строкой"):
            self._author: str = value

    @property
    def year(self) -> int:
        """Геттер для года издания книги."""
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        """Сеттер для года издания книги."""
        if Book.checking_the_integer(value, error="Год должен быть положительным числом"):
            self._year: int = value

    @property
    def genre(self) -> str:
        """Геттер для жанра книги."""
        return self._genre

    @genre.setter
    def genre(self, value: str) -> None:
        """Сеттер для жанра книги."""
        if Book.checking_the_string(value, error="Жанр должен быть строкой"):
            self._genre: str = value

    @property
    def pages(self) -> int:
        """Геттер для количества страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """Сеттер для количества страниц в книге."""
        if Book.checking_the_integer(value, error="Страница должна быть положительным числом"):
            self._pages: int = value

    @staticmethod
    def checking_the_integer(value: int, error: str) -> bool:
        """Статический метод для проверки значения. Значение должно быть не отрицательным числом."""
        if isinstance(value, int) and value >= 0:
            return True
        else:
            raise ValueError(error)

    @staticmethod
    def checking_the_string(value: str, error: str) -> bool:
        """Статический метод для проверки значения. Значение должно быть строкой."""
        if isinstance(value, str):
            return True
        else:
            raise ValueError(error)

    def __str__(self) -> str:
        """Неформальное представление книги."""
        return f'{self.title}, {self.author}, {self.year}, {self.genre}, {self.pages}'

    def __repr__(self) -> str:
        """Формальное представление книги."""
        return (f"Book(title='{self.title}', author='{self.author}', year={self.year}, genre='{self.genre}',"
                f" pages={self.pages})")


class Library:
    """Класс для создания библиотеки и работы с ней."""
    def __init__(self) -> None:
        """Создание библиотеки."""
        self.bookshelf: list = []

    def add_book(self, book) -> None:
        """Добавление книг в библиотеку."""
        self.bookshelf.append(book)

    def search_by_title(self, title: str) -> Union[Book, str]:
        """Поиск книги по названию."""
        for i in self.bookshelf:
            if i.title == title:
                return i
        return "Книга отсутствует в библиотеки"

    def get_books_by_author(self, author: str) -> list[Book]:
        """Список всех книг автора."""
        return [i for i in self.bookshelf if i.author == author]

    def get_books_sorted_by_year(self) -> list[Book]:
        """Отсортированый список по году выпуска."""
        return sorted(self.bookshelf, key=lambda x: x.year)

    def remove_book(self, book: str) -> str:
        """Удаление книги из библиотеки."""
        if book in self.bookshelf:
            list(self.bookshelf).remove(book)
        else:
            return "Книга отсутсвует в библиотеки"

    def __len__(self) -> int:
        """Метод возвращающий количество книг в бибилиотеки."""
        return len(self.bookshelf)

    def __repr__(self) -> str:
        """Формальное представление библиотеки."""
        return f"Library({self.bookshelf})"


library: Library = Library()
book1: Book = Book("Title1", "Author1", 2001, "Genre1", 300)
book2: Book = Book("Title2", "Author2", 1999, "Genre2", 150)
book3: Book = Book("Title3", "Author1", 2010, "Genre3", 400)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.search_by_title("Title1"))
print(library.get_books_by_author("Author1"))
print(library.get_books_sorted_by_year())
