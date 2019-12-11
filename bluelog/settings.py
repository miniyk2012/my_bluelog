class BaseConfig:
    pass


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
