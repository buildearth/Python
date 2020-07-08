# 银行接口
from db import db_handle
from lib import common

log = common.get_logger('bank')

# 提现接口
def withdrow_interface(user_name, money):
    user_dic = db_handle.select(user_name)

    balance = float(user_dic['balance'])
    money_and_fee = float(money) * 1.05

    # 检测余额是否充足
    if money_and_fee <= balance:
        # 更新余额
        balance -= money_and_fee
        user_dic['balance'] = balance

        # 记录流水
        flow = '用户 [{name}] 提现 [{money}] 手续费 [{fee}] 余额 [{balance}]]'.\
            format(name=user_name, money = money, fee = money_and_fee - float(money), balance = balance)
        user_dic['flow'].append(flow)
        log.info(flow)
        db_handle.save(user_dic)
        return True, flow
    else:
        return False, '用户余额不足, 请重新输入!'

# 转账接口
def tranfer_interface(user_name, dst_user, money):
    # 当前用户数据
    user_dic = db_handle.select(user_name)
    # 目标用户数据
    dst_user_dic = db_handle.select(dst_user)

    # 检测目标用户是否存在
    if not dst_user_dic:
        return False, '目标用户[%s]不存在'%dst_user

    # 检测当前用户金额是否充足
    balance = user_dic['balance']
    if balance < money:
        return False, '当前账户余额不足'

    # 数据更新
    user_dic['balance'] -= money
    dst_user_dic['balance'] += money

    # 记录流水
    flow = '用户[{user_name}]向[{dst_user}]转账[{money}]成功'.format(\
        user_name = user_name, dst_user = dst_user, money = money)
    user_dic['flow'].append(flow)
    dst_user_dic['flow'].append('接收到用户[{user_name}]转账的[{money}]'.format(\
        user_name = user_name, money = money))
    log.info(flow)
    db_handle.save(user_dic)
    db_handle.save(dst_user_dic)

    return True, flow

# 还款接口
def repay_interface(user_name, money):
    # 拿到用户数据
    user_dic = db_handle.select(user_name)

    # 更新金额
    user_dic['balance'] += money
    # 记录流水
    flow = '用户[%s] 还款[%s] 成功'% (user_name, money)
    user_dic['flow'].append(flow)
    log.info(flow)
    # 用户数据更新
    db_handle.save(user_dic)
    return True, flow

# 查看流水接口
def check_flow_interface(user_name):
    user_dic = db_handle.select(user_name)
    return user_dic['flow']


def pay_interface(user_name, cost):
    user_dic = db_handle.select(user_name)
    if user_dic['balance'] >= cost:
        # 支付操作
        user_dic['balance'] -= cost
        flow = '用户消费 %s'%cost
        user_dic['flow'].append(flow)
        log.info(flow)
        db_handle.save(user_dic)
        return True
    else:
        return False
