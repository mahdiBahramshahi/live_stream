from flask import Flask
from config import Development
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app , db)

from mod_users import users
app.register_blueprint(users)

from mod_admin import admin
app.register_blueprint(admin)

import views

