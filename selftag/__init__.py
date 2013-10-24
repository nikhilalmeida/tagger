"Initializes the tagger app"
from flask import Flask

import config

app = Flask(__name__)
app.config.from_object(config)

from views import views

app.register_blueprint(views)
