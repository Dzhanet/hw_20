from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, *movie_d):
        self.session.add(*movie_d)
        self.session.commit()
