import os
from conf import settings
from db import models
def get_all_school_info_interface():
    # 1.构造学校文件夹
    school_dir_path = os.path.join(settings.DB_PATH, 'School')

    # 2.检测文件夹是否存在,不存在,没有学校信息
    if not os.path.exists(school_dir_path):
        return None
    # 返回文件夹下的所有文件
    return os.listdir(school_dir_path)

def login_interface(user_name, password, sole):
    # 公共登录接口
    if sole == 'admin':
        obj = models.Admin.select(user_name)
    elif sole == 'student':
        obj = models.Student.select(user_name)
    elif sole == 'teacher':
        obj = models.Teacher.select(user_name)
    else:
        return False, '不支持的类型'

    if not obj:
        return False, '用户不存在'

    # 检测密码
    if password == obj.pwd:
        return True, '用户[{}]登录成功'.format(user_name)
    else:
        return False, '密码错误'

def get_course_by_school(school_name):
    school_obj = models.School.select(school_name)

    return school_obj.get_course()

def get_student_by_course(course_name):
    course_obj = models.Course.select(course_name)
    return course_obj.get_student()
