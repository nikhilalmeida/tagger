"""
Python Datastore API: http://code.google.com/appengine/docs/python/datastore/
"""

from google.appengine.ext import db
import util
import uuid


class Todo(db.Model):
    """Model to save a Todo to the GAE Datastore."""
    text = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)


class Picture():
    def __init__(self, url):
        self.url = url
        self.tags = []
        games_used = []


class Game():
    def __init__(self,player1, player2):
        self.players = [player1,player2]
        self.images = []
        self.pointsEarned = 0
        self.tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                    if unicodedata.category(unichr(i)).startswith('P'))
        self.game_id = uuid.uuid4()

    def add_picture(picture):
        self.images.append(picture)

    def validate(word1="", word2=""):
        if normalize_word(word1) == normalize_word(word2):
            self.picture.add_tag(word1)
            return True
        else:
            return False

    def new_round():
        # TODO: Pick random picture from the database.
        picture  = Picture()

        picture.games_used(self.game_id)

        return 



    def normalize_word(text):
        """
        strip input string of any punctuations, make it lowercase and
        return the stripped text.
        """
        if text:
            stripped = "".join(unicode(text).translate(tbl).lower().split())
            return stripped
