"""
Python Datastore API: http://code.google.com/appengine/docs/python/datastore/
"""

from google.appengine.ext import db


class Todo(db.Model):
    """Model to save a Todo to the GAE Datastore."""
    text = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)


class Counter():
    """Model to save a Todo to the GAE Datastore."""
    def __init__(self):
        self.count =0

    def increment(self):
        self.count+=1

    def get_counter(self):
        return self.count

class Picture(db.Model):
    pic_url = db.LinkProperty()
    taboo_words = db.

class Image():
    def __init__(self, url):
        self.url = url
        self.words = []


class Game():
    def __init__(self,player1, player2):
        self.players = [player1,player2]
        self.images = []
        self.pointsEarned = 0
