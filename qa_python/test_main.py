import pytest
from main import BooksCollector

class TestBooksCollector:

    def setup_method(self):
        """Создаем новый экземпляр перед каждым тестом для чистоты данных."""
        self.bc = BooksCollector()

    def test_add_new_book_success(self):
        self.bc.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in self.bc.books_genre
        assert self.bc.books_genre["Гарри Поттер"] == ""

    @pytest.mark.parametrize("name, expected_result", [
        ("", False),
        ("a" * 41, False),
        ("Книга", True),
    ])
    def test_add_new_book_validation(self, name, expected_result):
        self.bc.add_new_book(name)
        assert (name in self.bc.books_genre) == expected_result

    def test_set_book_genre_success(self):
        self.bc.add_new_book("Книга1")
        self.bc.set_book_genre("Книга1", "Фантастика")
        assert self.bc.get_book_genre("Книга1") == "Фантастика"

    def test_set_book_genre_invalid_genre(self):
        self.bc.add_new_book("Книга2")
        self.bc.set_book_genre("Книга2", "Фэнтези")
        # Жанр "Фэнтези" нет в списке self.genre, поэтому он не должен установиться
        assert self.bc.get_book_genre("Книга2") == ""

    def test_get_book_genre(self):
        self.bc.add_new_book("Книга3")
        self.bc.set_book_genre("Книга3", "Комедии")
        assert self.bc.get_book_genre("Книга3") == "Комедии"
        assert self.bc.get_book_genre("Не_существует") is None

    def test_get_books_with_specific_genre(self):
        self.bc.add_new_book("Книга4")
        self.bc.add_new_book("Книга5")
        self.bc.set_book_genre("Книга4", "Детективы")
        self.bc.set_book_genre("Книга5", "Детективы")
        result = self.bc.get_books_with_specific_genre("Детективы")
        assert result == ["Книга4", "Книга5"]

    def test_get_books_for_children(self):
        self.bc.add_new_book("Детектив")
        self.bc.add_new_book("Мультфильм")
        self.bc.add_new_book("Комедия")
        self.bc.set_book_genre("Детектив", "Детективы")
        self.bc.set_book_genre("Мультфильм", "Мультфильмы")
        self.bc.set_book_genre("Комедия", "Комедии")
        
        # Для детей подходят все, кроме тех, что в genre_age_rating (Ужасы, Детективы)
        result = self.bc.get_books_for_children()
        assert result == ["Мультфильм", "Комедия"]

    def test_add_book_in_favorites(self):
        self.bc.add_new_book("Книга6")
        self.bc.add_book_in_favorites("Книга6")
        assert "Книга6" in self.bc.favorites

        # Повторная попытка добавить ту же книгу не должна дублировать её
        self.bc.add_book_in_favorites("Книга6")
        assert self.bc.favorites.count("Книга6") == 1

    def test_delete_book_from_favorites(self):
        self.bc.add_new_book("Книга7")
        self.bc.add_book_in_favorites("Книга7")
        self.bc.delete_book_from_favorites("Книга7")
        assert "Книга7" not in self.bc.favorites

    def test_get_list_of_favorites_books(self):
        assert self.bc.get_list_of_favorites_books() == []

        self.bc.add_new_book("Книга8")
        self.bc.add_book_in_favorites("Книга8")
        assert self.bc.get_list_of_favorites_books() == ["Книга8"]
