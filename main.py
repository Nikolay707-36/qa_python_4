class BooksCollector:
    genre = {"Детективы", "Мультфильмы", "Комедии", "Фантастика"}
    genre_age_rating = {"Детективы", "Фантастика"}

    def __init__(self):
        self.books_genre = {}
        self.favorites = []

    def add_new_book(self, name: str):
        """Добавляет новую книгу без жанра."""
        if not name or len(name) > 40:
            return False
        if name not in self.books_genre:
            self.books_genre[name] = ""
            return True
        return False

    def set_book_genre(self, name: str, genre: str):
        """
        Устанавливает жанр, ТОЛЬКО если:
        1. Книга есть в словаре books_genre.
        2. Жанр есть в списке self.genre (разрешённые жанры).
        """
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name: str):
        """Выводит жанр книги по её имени."""
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre: str):
        """Выводит список книг с определённым жанром."""
        return [book for book, g in self.books_genre.items() if g == genre]

    def get_books_genre(self):
        """Выводит текущий словарь books_genre."""
        return self.books_genre

    def get_books_for_children(self):
        """
        Возвращает книги, которые подходят детям.
        У жанра книги не должно быть возрастного рейтинга.
        """
        result = []
        for book, g in self.books_genre.items():
            if g and g not in self.genre_age_rating:
                result.append(book)
        return result

    def add_book_in_favorites(self, name: str):
        """Добавляет книгу в избранное, если она есть в коллекции и ещё не в избранном."""
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def delete_book_from_favorites(self, name: str):
        """Удаляет книгу из избранного."""
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        """Получает список избранных книг."""
        return self.favorites

