from google.appengine.api import users
from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty()
    experience = ndb.IntegerProperty()
    level = ndb.IntegerProperty(default=0)  # Alternative shown in _level
    name = ndb.StringProperty()

    @property
    def games_played(self):
        # Query game.players
        return 0

    @property
    def games_won(self):
        # Query Game.winners
        return 0

    @property
    def win_percentage(self):
        # self.games_won / self.games_played
        games_played = self.games_played
        if games_played:
            return self.games_won / self.games_played
        else:
            return 0

    @property
    def _level(self):
        # Some algorithm that uses the amount of experience they have
        # to compute their level
        pass

    @staticmethod
    def get_current_user():
        google_user = users.get_current_user()
        if google_user:
            return User.query(User.email == google_user.email()).get()
        return None
