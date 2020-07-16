import os
import pickle

from conf import settings

def save(obj):
    # 1.构建数据存放的文件夹,以类名为文件夹名,user为对象名
    data_dir_path = os.path.join(settings.DB_PATH, obj.__class__.__name__)

    # 2.判断文件是否存在,不存在则创建
    if not os.path.exists(data_dir_path):
        os.mkdir(data_dir_path)

    # 3.构建文件路径
    user_file_path = os.path.join(data_dir_path, obj.user)

    with open(user_file_path, mode = 'wb') as f:
        pickle.dump(obj, f)

def select(cls, name):
    # 1.构建数据存放的文件夹,以类名为文件夹名,user为对象名
    data_dir_path = os.path.join(settings.DB_PATH, cls.__name__)

    # 2.构建文件路径
    user_file_path = os.path.join(data_dir_path, name)

    # 3.判断文件是否存在,不存在则用户名不存在
    if not os.path.exists(user_file_path):
        return None
    # 4.文件存在返回
    with open(user_file_path, mode = 'rb') as f:
        admin_onj = pickle.load(f)
    return admin_onj
