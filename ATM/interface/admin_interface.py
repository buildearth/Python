from db import db_handle
from lib import common

log = common.get_logger('admin')
def change_bal_interface(user_name, money):
    # 获取用户数据
    user_dic = db_handle.select(user_name)
    if not user_dic:
        return False, '用户不存在'

    # 修改额度并更新
    user_dic['balance'] = money
    flow = '额度修改为%s'%money
    user_dic['flow'].append(flow)
    db_handle.save(user_dic)
    log.info(flow)
    return True, '额度修改成功'

def lock_user_interface(user_name):
    user_dic = db_handle.select(user_name)
    if not user_dic:
        return False, '用户不存在'

    user_dic['locked'] = True
    log.info('用户[%s]被冻结'%user_name )
    db_handle.save(user_dic)
    return True, '冻结成功'
