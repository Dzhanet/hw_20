from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='First Director')
    d2 = Director(id=2, name='Second Director')
    d3 = Director(id=3, name='Third Director')

    directors = {1: d1, 2: d2, 3: d3}

    director_dao.get_one = MagicMock(side_effect=directors.get)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=d1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='First Genre')
    g2 = Genre(id=2, name='Second Genre')
    g3 = Genre(id=3, name='Third Genre')

    geners = {1: g1, 2: g2, 3: g3}

    genre_dao.get_one = MagicMock(side_effect=geners.get)
    genre_dao.get_all = MagicMock(return_value=geners.values())
    genre_dao.create = MagicMock(return_value=g1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='First Movie', description='Description',
               trailer='link', year=2000, rating=10.0, genre_id=1, director_id=1)
    m2 = Movie(id=2, title='Second Movie', description='Description',
               trailer='link', year=2000, rating=10.0, genre_id=1, director_id=1)
    m3 = Movie(id=3, title='Third Movie', description='Description',
               trailer='link', year=2000, rating=10.0, genre_id=1, director_id=1)

    movies = {1: m1, 2: m2, 3: m3}

    movie_dao.get_one = MagicMock(side_effect=movies.get)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=1, title='First Movie'))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
