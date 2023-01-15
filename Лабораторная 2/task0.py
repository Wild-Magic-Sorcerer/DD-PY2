class Book(object):
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}"

    def __repr__(self):
        return f"Book(id={self.id}, name={self.name!r}, pages={self.pages})"


class Library(object):
    def __init__(self, books: list[Book] = None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books):
            return self.books[-1].id + 1
        else:
            return 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book_id == book.id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует.")
