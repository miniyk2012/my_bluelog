# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension

bootstrap = Bootstrap()
db = SQLAlchemy()
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
migrate = Migrate()
toolbar = DebugToolbarExtension()

