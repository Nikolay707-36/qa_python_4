import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_book(self, books_collector):
        books_collector.add_new_book("Тест")
        assert "Тест" in books_collector.books_genre
        assert books_collector.books_genre["Тест"] == ""

    def test_add_new_book_success(self, books_collector):
        books_collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in books_collector.books_genre
        assert books_collector.books_genre["Гарри Поттер"] == ""

    @pytest.mark.parametrize("name, expected_result", [
        ("", False),
        ("a" * 41, False),
        ("Книга", True),
    ])
    def test_add_new_book_validation(self, name, expected_result, books_collector):
        result = books_collector.add_new_book(name)
        
        if expected_result:
            assert result is True
            assert name in books_collector.books_genre
        else:
            assert result is False
            assert name not in books_collector.books_genre

    def test_set_book_genre_success(self, books_collector):
        books_collector.add_new_book("Книга1")
        books_collector.set_book_genre("Книга1", "Фантастика")
        assert books_collector.get_book_genre("Книга1") == "Фантастика"

    def test_set_book_genre_invalid_genre(self, books_collector):
        books_collector.add_new_book("Книга2")
        books_collector.set_book_genre("Книга2", "Фэнтези")
        current_genre = books_collector.get_book_genre("Книга2")
        assert current_genre == "" or current_genre is None

    def test_get_book_genre(self, books_collector):
        books_collector.add_new_book("Книга3")
        books_collector.set_book_genre("Книга3", "Комедии")
        
        assert books_collector.get_book_genre("Книга3") == "Комедии"
        assert books_collector.get_book_genre("Не_существует") is None

    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book("Книга4")
        books_collector.add_new_book("Книга5")
        books_collector.set_book_genre("Книга4", "Детективы")
        books_collector.set_book_genre("Книга5", "Детективы")
        
        result = books_collector.get_books_with_specific_genre("Детективы")
        assert set(result) == {"Книга4", "Книга5"}

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book("Детектив")
        books_collector.add_new_book("Мультфильм")
        books_collector.add_new_book("Комедия")
        books_collector.set_book_genre("Детектив", "Детективы")
        books_collector.set_book_genre("Мультфильм", "Мультфильмы")
        books_collector.set_book_genre("Комедия", "Комедии")
        
        result = books_collector.get_books_for_children()
        assert set(result) == {"Мультфильм", "Комедия"}

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book("Книга6")
        books_collector.add_book_in_favorites("Книга6")
        assert "Книга6" in books_collector.favorites
        books_collector.add_book_in_favorites("Книга6")
        assert books_collector.favorites.count("Книга6") == 1

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Книга7")
        books_collector.add_book_in_favorites("Книга7")
        books_collector.delete_book_from_favorites("Книга7")
        assert "Книга7" not in books_collector.favorites

    def test_get_list_of_favorites_books(self, books_collector):
        assert books_collector.get_list_of_favorites_books() == []
        books_collector.add_new_book("Книга8")
        books_collector.add_book_in_favorites("Книга8")
        assert books_collector.get_list_of_favorites_books() == ["Книга8"]

    def test_get_books_genre(self, books_collector):
        books_collector.add_new_book("Книга1")
        books_collector.add_new_book("Книга2")
        books_collector.set_book_genre("Книга1", "Детективы")
        books_collector.set_book_genre("Книга2", "Комедии")

        result = books_collector.get_books_genre()

        expected = {"Книга1": "Детективы", "Книга2": "Комедии"}
        assert result == expected


