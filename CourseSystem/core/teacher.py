from lib import common
from interface import teacher_interface
from interface import common_interface
teacher_info = {
    'user': None
}


# 登录
def login():
    while True:
        # 1.获取用户输入的名字和密码
        user_name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()

        flag, msg = common_interface.login_interface(user_name, password, 'teacher')
        print(msg)
        if flag:
            teacher_info['user'] = user_name
            break
# 2.查看所有课程
@common.auth('teacher')
def check_course():
    # 查看老师教授的所有课程
    course_list = teacher_interface.teacher_check_course_interface(teacher_info.get('user'))
    if not course_list:
        print('老师没有选择任何课程')
    print(course_list)

# 3.选择教授课程
@common.auth('teacher')
def select_course():
    while True:
        # 老师选择学校
        school_list = common_interface.get_all_school_info_interface()
        if not school_list:
            print('没有学校,请联系管理员')

        for index, school_name in enumerate(school_list):
            print('编号:{}  学校名字:{}'.format(index, school_name))

        school_choice = input('请输入学校编号:').strip()
        if not school_choice.isdigit():
            print('请输入正确的编号')
            continue

        school_choice = int(school_choice)
        if school_choice not in range(len(school_list)):
            print('请输入正确的编号')
            continue

        school_name = school_list[school_choice]

        # 打印学校所有课程
        course_list = common_interface.get_course_by_school(school_name)
        if not course_list:
            print('没有课程,请联系管理员')

        for index, course_name in enumerate(course_list):
            print('编号:{}  课程名字:{}'.format(index, course_name))

        # 老师选择教授课程
        course_choice = input('请输入课程编号:').strip()
        if not course_choice.isdigit():
            print('请输入正确的编号')
            continue

        course_choice = int(course_choice)
        if course_choice not in range(len(course_list)):
            print('请输入正确的编号')
            continue

        course_name = course_list[course_choice]

        # 保存老师的选择
        flag, msg = teacher_interface.teacher_choice_course_interface(course_name, teacher_info.get('user'))
        print(msg)
        break


# 4.查看课程下的学生
@common.auth('teacher')
def check_course_students():
    while True:
        # 获取所有课程信息,老师选择课程
        course_list = teacher_interface.teacher_check_course_interface(teacher_info.get('user'))
        if not course_list:
            print('没有课程,请联系管理员')
            break

        for index, course_name in enumerate(course_list):
            print('编号:{}  课程名字:{}'.format(index, course_name))
            break

        # 老师选择教授课程
        course_choice = input('请输入课程编号:').strip()
        if not course_choice.isdigit():
            print('请输入正确的编号')
            continue

        course_choice = int(course_choice)
        if course_choice not in range(len(course_list)):
            print('请输入正确的编号')
            continue

        course_name = course_list[course_choice]
        # 打印课程下的所有学生
        student_list = common_interface.get_student_by_course(course_name)
        print(student_list)
        break


# 5.修改分数
@common.auth('teacher')
def change_score():
    while True:
        # 选择课程
        course_list = teacher_interface.teacher_check_course_interface(teacher_info.get('user'))
        if not course_list:
            print('老师没有选择任何课程')
            break
        for index, course_name in enumerate(course_list):
            print('编号:{}  课程名字:{}'.format(index, course_name))

        course_choice = input('请输入课程编号:').strip()
        if not course_choice.isdigit():
            print('请输入正确的编号')
            continue

        course_choice = int(course_choice)
        if course_choice not in range(len(course_list)):
            print('请输入正确的编号')
            continue

        course_name = course_list[course_choice]
        # 选择学生
        student_list = common_interface.get_student_by_course(course_name)
        if not student_list:
            print('该课程下没有任何学生')
            break
        for index, student_name in enumerate(student_list):
            print('编号:{}  学生名字:{}'.format(index, student_name))

        student_choice = input('请输入学生编号:').strip()
        if not student_choice.isdigit():
            print('请输入正确的编号')
            continue

        student_choice = int(student_choice)
        if student_choice not in range(len(student_list)):
            print('请输入正确的编号')
            continue

        student_name = student_list[student_choice]

        # 修改学生分数
        while True:
            score = input('请输入学生的分数:').strip()
            if not score.isdigit():
                print('请输入正确的分数')
            else:
                break
        # 保存学生分数
        teacher_interface.teacher_change_score_interface(
            student_name, course_name, score, teacher_info.get('user'))
        break


func_dic = {
    '1': login,
    '2': check_course,
    '3': select_course,
    '4': check_course_students,
    '5': change_score,
}

def teacher_view():
    while True:
        print('''
            1.登录
            2.查看所有课程
            3.选择教授课程
            4.查看课程下的学生
            5.修改分数
        ''')

        choice = input('请输入功能编号:').strip()

        if choice == 'q':
            break

        if not choice in func_dic:
            print('请输入正确的功能编号!')
            continue

        # 执行功能
        func_dic.get(choice)()
