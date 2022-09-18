import pytest

from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(1) is not None
        assert self.director_service.get_one(1).name == 'First Director'

    def test_get_all(self):
        assert self.director_service.get_all() is not None
        assert len(self.director_service.get_all()) > 0

    def test_create(self):
        d1 = {'name': 'First Director'}
        assert self.director_service.create(d1) is not None
        assert self.director_service.create(d1).name == d1.get('name')

    def test_update(self):
        d1 = {'id': 1, 'name': 'New Name'}
        assert self.director_service.update(d1)

    def test_partial_update(self):
        d1 = {'id': 1, 'name': 'New Name'}
        assert self.director_service.partially_update(d1)

    def test_delete(self):
        self.director_service.delete(1)
