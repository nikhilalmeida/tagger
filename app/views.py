"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""

from google.appengine.api import mail
from decorators import login_required
from flask import Blueprint, url_for, render_template, request, redirect, jsonify
from models import Todo
from forms import TodoForm, EmailForm
import Queue

views = Blueprint('views', __name__)
total_users = 1
queue = []
games = {}
current_players = {}


@views.route('/')
def index(user_id=None):
    """Render website's index page."""
    # return render_template('index.html')
    
    # return jsonify({"hello":"world"})
    global total_users
    if user_id is None:
        user_id = total_users
        total_users += 1
    # return  redirect(url_for('game_list')'')
    return  redirect('/game/abc')



@views.route('/game/{user_id}')
def game_list(user_id=None):
    """Simple todo page."""

    if len(queue) is 0:
        queue.append(user_id)
        render_template('game.html', user_id=user_id, message="refresh till a new user comes along")
    else:
        game = create_new_game(user_id)
   
    return render_template('game.html', form=form)

def create_new_game(user_id):
    opponent_id = queue[0]
    queue.remove(opponent_id)
    game= Game(user_id,opponent_id)
    games[game.get_id()] = game
    current_players[user_id] = game.get_id()
    current_players[opponent_id] = game.get_id()


@views.route('/game/leave/{user_id}/{game_id}')
def leave_game(user_id,game_id):
    game = games[game_id]
    #TODO: Store game state.
    games.remove(game_id)
    current_players.pop(user_id)


@views.route('/game/add/{user_id}', methods=["POST"])
def submit_word(user_id):
    """Add a todo."""
    form = TodoForm()

    if request.method == 'POST' and form.validate_on_submit():
        todo = Todo(text=form.todo.data)
        todo.save()
    return redirect(url_for('game_list'))



@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

