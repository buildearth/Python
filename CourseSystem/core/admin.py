from interface import admin_interface
from lib import common
from interface import common_interface
admin_info = {
    'user': None
}

# 注册功能
def register():
    while True:
        # 1.获取用户输入的名字和密码
        user_name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请再次输入密码:').strip()

        # 2小逻辑
        # 2.1 检测用户名和密码是否为空
        if user_name == '' or password == '':
            print('用户名和密码不能为空,请重新输入!')
            continue
        # 2.2.检测用户输入的两次密码是否一致
        if password != re_password:
            print('两次输入密码不一致,请重新输入!')
            continue
        # 3.调用管理员接口
        flag, msg = admin_interface.admin_register_interface(user_name, password)
        print(msg)
        if flag:
            break

# 2.登录
def login():
    while True:
        # 1.获取用户输入的名字和密码
        user_name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        # 2.调用管理员接口
        flag, msg = common_interface.login_interface(user_name, password, 'admin')
        print(msg)
        if flag:
            admin_info['user'] = user_name
            break

# 3.创建学校
@common.auth('admin')
def creat_school():
    while True:
        school_name =  input('请输入学校的名字:').strip()
        school_addr =  input('请输入学校的地址:').strip()

        flag, msg = admin_interface.admin_create_school_interface(
            school_name, school_addr, admin_info.get('user'))

        print(msg)
        if flag:
            break


# 4.创建课程
@common.auth('admin')
def create_course():
    while True:
        # 1.获取学校信息
        school_list = common_interface.get_all_school_info_interface()
        # 1.1判断是否有学校
        if not school_list:
            print('没有任何学校存在,请联系管理员')

        # 1.2打印学校信息,供用户选择
        for index, name in enumerate(school_list):
            print('编号:{}  学校名字:{}'.format(index, name))

        # 2.选择学校
        # 2.1获取用户选择
        choice = input('请输入学校编号:').strip()

        # 2.2检测是否是数字构成
        if not choice.isdigit():
            print('请输入正确的功能编号')
            continue
        choice = int(choice)

        # 2.3检测输入是否超出范围
        if not choice in range(len(school_list)):
            print('请输入正确的功能编号')
            continue

        # 3.用户输入创建课程的名字
        course_name =  input('请输入要创建课程的名字:').strip()

        # 4.调用管理员接口,创建课程
        flag, msg = admin_interface.admin_create_course_interface(
            course_name, school_list[choice], admin_info.get('user'))

        print(msg)
        if flag:
            break

# 5.创建讲师
@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入讲师的名字:').strip()
        # 调用管理员接口创建讲师
        flag, msg = admin_interface.admin_create_teacher_interface(
            teacher_name, admin_info.get('user'))
        print(msg)
        if flag:
            break

func_dic = {
    '1': register,
    '2': login,
    '3': creat_school,
    '4': create_course,
    '5': create_teacher,
}

def admin_view():
    while True:
        print('''
            1.注册
            2.登录
            3.创建学校
            4.创建课程
            5.创建讲师
        ''')

        choice = input('请输入功能编号:').strip()

        if choice == 'q':
            break

        if not choice in func_dic:
            print('请输入正确的功能编号!')
            continue

        # 执行功能
        func_dic.get(choice)()
