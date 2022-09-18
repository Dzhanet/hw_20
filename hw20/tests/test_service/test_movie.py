import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(1).title == 'First Movie'

    def test_get_all(self):
        assert self.movie_service.get_all() is not None
        assert len(self.movie_service.get_all()) > 0

    def test_create(self):
        m1 = {
            'title': 'First Movie',
            'description': 'Description',
            'trailer': 'link',
            'year': 2000,
            'rating': 10.0,
            'genre_id': 1,
            'director_id': 1
        }
        assert self.movie_service.create(m1) is not None
        assert self.movie_service.create(m1).title == m1.get('title')

    def test_update(self):
        m1 = {
            'id': 1,
            'title': 'First Movie',
            'description': 'Description',
            'trailer': 'link',
            'year': 2000,
            'rating': 10.0,
            'genre_id': 1,
            'director_id': 1
        }
        self.movie_service.update(m1)

    def test_partial_update(self):
        m1 = {
            'id': 1,
            'title': 'New title'
        }
        self.movie_service.partially_update(m1)

    def test_delete(self):
        self.movie_service.delete(1)
