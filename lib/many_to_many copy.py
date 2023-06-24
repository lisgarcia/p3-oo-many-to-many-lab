## my code
class Author:
    
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)


class Book:
    
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)



class Contract:
    
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author (self, author):
        if not isinstance(author, Author):
            raise Exception
        else:
            self._author = author

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception
        else:
            self._book = book

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception
        else:
            self._date = date

    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalaties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception
        else:
            self._royalties = royalties