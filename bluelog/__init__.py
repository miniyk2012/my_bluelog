import os

from flask import Flask

from bluelog.settings import config
from bluelog.blueprints.blog import blog_bp

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

    return app


def register_logging(app):
    pass


def register_extensions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(blog_bp)


def register_errors(app):
    pass


def register_shell_context(app):
    pass


def register_template_context(app):
    pass


def register_request_handlers(app):
    pass


def register_commands(app):
    pass
