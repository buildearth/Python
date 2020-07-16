

def auth(sole):
    def login_auth(func):
        def inner(*args, **kwargs):
            from core import admin
            from core import student
            from core import teacher
            if sole == 'admin':
                if admin.admin_info.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('未登录,请先登录!')
                    admin.login()
            elif sole == 'teacher':
                if teacher.teacher_info.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('未登录,请先登录!')
                    teacher.login()
            elif sole == 'student':
                if student.student_info.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('未登录,请先登录!')
                    student.login()
            else:
                print('该视图不支持')
        return inner
    return login_auth
