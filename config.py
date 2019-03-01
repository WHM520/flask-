import logging
from redis import StrictRedis


class Config(object):
    SECRET_KEY = "iECgbYWReMNxkRprrzMo5KAQYnb2UeZ3bwvReTSt+VSESW0OB8zbglT+6rEcDW9X"
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # 保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定Session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    #  设置日志等级
    LOG_LEVEL = logging.DEBUG

# 开发配置
class DevelopmentConfig(Config):
    DEBUG = True

# 生产测试
class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = logging.WARNING

# 单元测试
class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
