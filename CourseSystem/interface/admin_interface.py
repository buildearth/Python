from db import models


def admin_register_interface(user_name, password):
    # 1.检测用户是否存在
    admin_obj = models.Admin.select(user_name)

    # 1.1用户存在,返回False,
    if admin_obj:
        return False, '用户已存在!'

    # 1.2用户不存在,调用创建管理员对象,pickle保存到文件
    admin_obj = models.Admin(user_name, password)
    admin_obj.save()
    return True, '用户[{}]创建成功!'.format(user_name)

def admin_login_interface(user_name, password):
    # 1.检测用户是否存在
    if not models.Admin.select(user_name):
        return False, '用户不存在!'

    # 2.获取管理员对象
    admin_obj = models.Admin.select(user_name)

    # 3.检测密码
    if password == admin_obj.pwd:
        return True, '用户[{}]登录成功!'.format(user_name)
    else:
        return False, '用户密码输入错误!'

def admin_create_school_interface(school_name, school_addr, admin_name):
    # 1.检测学校是否存在
    school_obj = models.School.select(school_name)
    # 2.存在,返回创建失败
    if school_obj:
        return False, '学校已经存在'

    # 3.管理创建学校
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_addr)
    return True, '学校[{}]创建成功'.format(school_name)

def admin_create_course_interface(course_name, school_name, admin_name):
    # 检测课程是否存在
    school_obj = models.School.select(school_name)

    if course_name in school_obj.course_list:
        return False, '课程已经存在于学校'

    # 管理员创建课程,并关联学校
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(course_name, school_obj)
    return True, '课程创建成功'

def admin_create_teacher_interface(teacher_name, admin_name, teacher_pwd = '123'):
    # 判断讲师是否存在
    teacher_obj = models.Teacher.select(teacher_name)

    if teacher_obj:
        return False, '讲师已经存在'

    # 管理员创建讲师
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, '讲师创建成功'
