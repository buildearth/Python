#数据处理层代码
import json
import os
from conf import settings

# 从json文件中选择数据
def select(user_name):
    # 构建用户数据存储路径
    file_name = os.path.join(settings.USER_DATA_PATH, '%s.json'%user_name)

    # 判断文件是否存在->使用os的那个方法不清楚(****)
    if os.path.exists(file_name):
        # 检测用户密码的正确性
        with open(file_name, mode = 'rt', encoding = 'utf-8') as f:
            user_dic = json.load(f)
            return user_dic

    return None

# 信息存储或更新
def save(user_dic):
    # 构建用户信息存储路径
    user_name = user_dic['user_name']
    file_name = os.path.join(settings.USER_DATA_PATH, '%s.json'%user_name)

    with open(file_name, mode = 'wt', encoding = 'utf-8') as f:
        json.dump(user_dic, f, ensure_ascii = False)

# 读取商品信息
def read_shop_info():
    shop_path = os.path.join(settings.SHOP_DATA_PATH, 'food_store.json')
    with open(shop_path, mode = 'rt', encoding = 'utf-8') as f:
        shop_dic = json.load(f)

    return shop_dic
