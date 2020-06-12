# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
ckeditor = CKEditor()
csrf = CSRFProtect()
mail = Mail()
moment = Moment()
migrate = Migrate()
toolbar = DebugToolbarExtension()
login_manager = LoginManager()

# 使用login_required装饰器的视图, 若未登陆, 会自动重定向到指定页面, 并闪现消息提示, 配置如下:
login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登陆!'
login_manager.login_message_category = 'warning'


@login_manager.user_loader
def load_user(user_id):
    from my_bluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
