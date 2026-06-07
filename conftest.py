import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()
