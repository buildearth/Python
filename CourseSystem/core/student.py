from lib import common
from interface import student_interface
from interface import common_interface
student_info = {
    'user': None
}

# 注册功能
def register():
    while True:
        user_name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请再次输入密码:').strip()

        # 判断两次密码是否一致
        if not password == re_password:
            print('两次密码输入不一致,请重新输入')
            continue

        # 调用逻辑接口层,处理注册
        flag, msg = student_interface.student_register_interface(
            user_name, password)

        print(msg)
        if flag:
            break

# 2.登录
def login():
    while True:
        # 1.获取用户输入的名字和密码
        user_name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()

        flag, msg = common_interface.login_interface(user_name, password, 'student')
        print(msg)
        if flag:
            student_info['user'] = user_name
            break

# 3.选择学校
@common.auth('student')
def select_school():
    while True:
        # 获取学校信息,展示给学生让学生选择学校
        school_list = common_interface.get_all_school_info_interface()
        if not school_list:
            print('没有学校存在,请联系管理员')
            break

        for index, school_name in enumerate(school_list):
            print('编号:{}  学校名字:{}'.format(index, school_name))

        choice = input('请输入学校编号:').strip()

        # 检测choice的正确性
        if not choice.isdigit():
            print('请输入正确的编号')
            continue

        choice = int(choice)
        if not choice in range(len(school_list)):
            print('请输入正确的编号')
            continue

        school_name = school_list[choice]
        # 调用接口层保存学生的选择
        flag, msg = student_interface.student_choice_school_interface(
            school_name, student_info.get('user'))

        print(msg)
        break

# 4.选择课程
@common.auth('student')
def select_course():
    while True:
        # 展示学生选择学校中的课程供学生选择,存在学生还没有选择学校的情况
        # 调用接口层获取学生选择学校的信息
        school_name = student_interface.student_check_school(student_info.get('user'))
        if not school_name:
            print('学生没有选择学校,请先选择学校')
            break
        # 从学校中拿出所有课程让学生选择
        course_list = common_interface.get_course_by_school(
            school_name)
        if not course_list:
            print('该学校没有课程,请联系管理员')
            break

        # 打印课程
        for index,course_name in enumerate(course_list):
            print('编号:{}  课程名称:{}'.format(index, course_name))
        # 学生选择课程
        choice = input('请输入课程编号:').strip()
        if not choice.isdigit():
            print('请输入正确的课程编号')
            continue

        choice = int(choice)
        if choice not in range(len(course_list)):
            print('请输入正确的课程编号')
            continue

        course_name = course_list[choice]
        flag,msg = student_interface.student_choice_course_interface(
            course_name, student_info.get('user'))
        print(msg)
        break

# 5.查看分数
@common.auth('student')
def check_score():
    score = student_interface.student_get_score_interface(student_info.get('user'))
    print(score)

func_dic = {
    '1': register,
    '2': login,
    '3': select_school,
    '4': select_course,
    '5': check_score,
}

def student_view():
    while True:
        print('''
            1.注册
            2.登录
            3.选择校区
            4.选择课程
            5.查看分数
        ''')

        choice = input('请输入功能编号:').strip()

        if choice == 'q':
            break

        if not choice in func_dic:
            print('请输入正确的功能编号!')
            continue

        # 执行功能
        func_dic.get(choice)()
