import os

from flask import Flask, render_template

from bluelog.blueprints.admin import admin_bp
from bluelog.blueprints.blog import blog_bp
from bluelog.commands import register_commands
from bluelog.extensions import db, migrate, bootstrap, mail, toolbar
from bluelog.models import Admin, Category
from bluelog.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blueblog')
    app.config.from_object(config.get(config_name, 'development'))

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    register_shell_context(app)
    register_template_context(app)
    register_request_handlers(app)
    print('create app Done.')
    return app


def register_logging(app):
    pass


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)


def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500


def register_shell_context(app):
    pass


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        return dict(admin=admin, categories=categories)


def register_request_handlers(app):
    pass
