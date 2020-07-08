# 存放公共方法
from core import src
from conf import settings
from logging import getLogger, config

def login_auth(func):
    def wrapper(*args, **kwargs):
        if src.login_user:
            # 认证了才能进行的操作
            res = func(*args, **kwargs)
            return res
        else:
            # 没有登录,先进行登录
            print('用户没有登录,无法使用功能')
            src.login()
    return wrapper

def get_logger(log_type):
    config.dictConfig(settings.LOGGING_DIC)
    return getLogger(log_type)
