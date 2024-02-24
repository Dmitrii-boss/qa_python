import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')

        assert collector.get_books_genre() == {'Гарри Поттер и философский камень': ''}

    def test_add_duplicate_book(self):
        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('1984')

        collector.set_book_genre('1984', 'Фантастика')

        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_invalid_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Тень ветра')

        collector.set_book_genre('Тень ветра', 'Драма')

        assert collector.get_book_genre('Тень ветра') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Тихое место')
        collector.set_book_genre('Тихое место', 'Ужасы')

        result = collector.get_books_with_specific_genre('Фантастика')

        assert result == ['Дюна']

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Красная шапочка')
        collector.set_book_genre('Красная шапочка', 'Детективы')
        collector.add_new_book('Пеппа Пиг')
        collector.set_book_genre('Пеппа Пиг', 'Мультфильмы')

        result = collector.get_books_for_children()

        assert result == ['Пеппа Пиг']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и узник Азкабана')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и узник Азкабана']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Над пропастью во ржи')
        collector.add_book_in_favorites('Над пропастью во ржи')
        collector.delete_book_from_favorites('Над пропастью во ржи')

        assert collector.get_list_of_favorites_books() == []

    def test_add_book_to_favorites_invalid_book(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Таинственная книга')

        assert collector.get_list_of_favorites_books() == []

