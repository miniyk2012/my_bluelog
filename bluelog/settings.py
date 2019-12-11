import os
from pathlib import Path

basedir = str(Path(__file__).parents[1])


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    DEBUG_TB_INTERCEPT_REDIRECTS = False  # debug bar不拦截重定向

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True  # 似乎是用来决定是否打印数据库log的

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'


class DevelopmentConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'test': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
