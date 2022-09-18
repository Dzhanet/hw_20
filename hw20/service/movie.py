from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()
    
    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        return self.dao.update(movie_d)

    def partially_update(self, *movie_d):
        self.dao.update(*movie_d)

    def delete(self, rid):
        self.dao.delete(rid)