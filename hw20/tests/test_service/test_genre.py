import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        assert self.genre_service.get_one(1) is not None
        assert self.genre_service.get_one(1).name == 'First Genre'

    def test_get_all(self):
        assert self.genre_service.get_all() is not None
        assert len(self.genre_service.get_all()) > 0

    def test_create(self):
        g1 = {'name': 'First Genre'}
        assert self.genre_service.create(g1) is not None
        assert self.genre_service.create(g1).name == g1.get('name')

    def test_update(self):
        d1 = {'id': 1, 'name': 'New Genre'}
        assert self.genre_service.update(d1)

    def test_partial_update(self):
        d1 = {'id': 1, 'name': 'New Genre'}
        assert self.genre_service.partially_update(d1)

    def test_delete(self):
        self.genre_service.delete(1)
