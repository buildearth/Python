# 用户视图层的接口
from db import db_handle

def register_interface(user_name, password, balance = 15000):
    # 1.判断用户是否存在
    # 2.注册信息存储

    #从数据处理层获取user_name的信息
    user_dic = db_handle.select(user_name)
    if user_dic:
        return False, '用户已经存在，请重新输入'

    # 用户可以注册，构造用户信息
    user_dic = {
        'user_name': user_name,
        'password': password,
        'balance': balance,
        # 记录购物车信息
        'shop_car': {},
        # 记录用户流水信息
        'flow': [],
        # 账户是否冻结，True:冻结, False:没有冻结
        'locked': False
    }

    db_handle.save(user_dic)
    return True, '用户 [%s] 注册成功'%user_name

def login_interface(user_name, password):
    # 调用数据处理层，拿到user_name对应的数据
    user_dic = db_handle.select(user_name)
    if user_dic:
        # 检测用户是否被冻结
        if user_dic['locked'] == True:
            return False, '用户 [%s] 被冻结'%user_name
        # 检测密码
        if password == user_dic['password']:
            # 密码匹配成功
            return True, '用户 [%s] 登录成功'%user_name
        else:
            return False, '密码错误，请重新输入'
    else:
        return False, '用户名不存在，请重新输入'

def check_bal_interface(user_name):
    # 获取用户数据信息
    user_dic = db_handle.select(user_name)
    return user_dic['balance']
