class Book(object):
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if (not isinstance(name, str)) or (not isinstance(author, str)):
            raise TypeError("Недопустимый тип")
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Недопустимый тип")
        elif pages <= 0:
            raise ValueError("Недопустимое значение")
        else:
            self._pages = pages

    def __str__(self):
        """ Да, можно не перегружать, если не нужна информация о числе страниц. """
        return f"Бумажная книга {self._name}. Автор {self._author}. Число страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, val):
        if not isinstance(val, int):
            raise TypeError("Недопустимый тип")
        elif val <= 0:
            raise ValueError("Недопустимое значение")
        else:
            self._pages = val


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Недопустимый тип")
        elif duration <= 0:
            raise ValueError("Недопустимое значение")
        else:
            self._duration = duration

    def __str__(self):
        """ Да, можно не перегружать, если не нужна информация о длительности. """
        return f"Аудиокнига {self._name}. Автор {self._author}. Длительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, val):
        if not isinstance(val, float):
            raise TypeError("Недопустимый тип")
        elif val <= 0:
            raise ValueError("Недопустимое значение")
        else:
            self._duration = val


a = Book(name="123", author="321")
print(a.__str__())
print(a.__repr__())
print(a.name)
print(a.author, "\n")

b = PaperBook(name="Sass", author="Bass", pages=3)
print(b.__str__())
print(b.__repr__())
print(b.name)
print(b.author)
print(b.pages)
b.pages = 666
print(b.pages, "\n")

c = AudioBook(name="Fuff", author="Puff", duration=666.666)
print(c.__str__())
print(c.__repr__())
print(c.name)
print(c.author)
print(c.duration)
c.duration = 0.001
print(c.duration)
