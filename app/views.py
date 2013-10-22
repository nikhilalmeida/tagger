"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""

from google.appengine.api import mail
from decorators import login_required
from flask import Blueprint, url_for, render_template, request, redirect, jsonify
from models import Todo, Counter
from forms import TodoForm, EmailForm
import Queue

views = Blueprint('views', __name__)
counter = Counter()
total_users = 1
queue = []
games = {}
current_players = {}


@views.route('/')
def index():
    """Render website's index page."""
    # return render_template('index.html')
    counter.increment()
    return jsonify({"hello":"world", "count":counter.get_counter()})



@views.route('/game/{user_id}')
def todo_list(user_id):
    """Simple todo page."""
    if user_id is None:
        user_id = total_users
        total_users += 1
    form = TodoForm()
    if len(queue) is 0:
        queue.append(user_id)
        render_template('wait.html',user_id=user_id)
    else:
        opponent_id = queue[0]
        queue.remove(opponent_id)
        game= Game(user_id,opponent_id)
        games[game.get_id()] = game
        current_players[user_id] = game.get_id()
        current_players[user_id] = game.get_id()
    todos = Todo.all().order('-created_at')
    for todo in todos:
        print todo.text
    counter.increment()
    print "hello world, ", counter.get_counter()
    return render_template('todo.html', form=form, todos=todos)

@views.route('/game/leave/{user_id}/{game_id}')
def leave_game(user_id,game_id):
    game = games[game_id]
    #TODO: Store game state.
    games.remove(game_id)
    current_players.pop(user_id)


@views.route('/todo/add/{user_id}', methods=["POST"])
def add_todo():
    """Add a todo."""
    form = TodoForm()

    if request.method == 'POST' and form.validate_on_submit():
        todo = Todo(text=form.todo.data)
        todo.save()
    return redirect(url_for('todo_list'))

@login_required
@views.route('/email/')
def email():
    """Render a form for sending email."""
    form = EmailForm()
    return render_template('email.html', form=form)


@views.route('/email/someone/', methods=['POST'])
def email_someone():
    """
    This function actually emails the message.

    Make sure you change the from_address variable if you want to use this
    functionality -- otherwise it won't work.
    """
    form = EmailForm()
    if request.method == 'POST' and form.validate_on_submit():
        from_address = form.name.data + '@<YOURAPPID>.appspotmail.com'
        to_address = form.recipient.data
        subject = "%s <%s>" % (form.name.data, form.email.data)
        message = ("From: %s\n\n"
                   "Email: %s\n\n"
                   "Message: %s") % (form.name.data, form.email.data,
                                     form.message.data)
        mail.send_mail(sender=from_address, to=to_address,
                       subject=subject, body=message)
        status = 'success'
    else:
        status = 'failed'
    return redirect(url_for('email_status', status=status))


@views.route('/email/<status>/')
def email_status(status):
    """Render a success or failed status for the email."""
    return render_template('email_status.html', status=status)


@views.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')


@views.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

