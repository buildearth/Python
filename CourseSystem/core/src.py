'''
主程序视图
    1.管理员功能
    2.学生功能
    3.老师功能
'''
from core import admin
from core import student
from core import teacher

func_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}

def run():
    while True:
        print('''
            ======   选课系统   ======
                1.管理员功能
                2.学生功能
                3.老师功能
            ======     end     ======
        ''')

        choice = input('请输入功能编号:').strip()

        if choice == 'q':
            break

        # 检测输入正确性,根据功能字典
        if not choice in func_dic:
            print('请输入正确的功能编号!')
            continue

        # 执行功能
        func_dic.get(choice)()
