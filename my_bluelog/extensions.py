# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
migrate = Migrate()
toolbar = DebugToolbarExtension()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from my_bluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
