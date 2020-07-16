from db import models

def student_register_interface(user_name, password):
    # 检测学生是否已经注册
    student_obj = models.Student.select(user_name)

    if student_obj:
        return False, '学生[{}]已经注册过'.format(user_name)

    # 进行学生信息保存
    student_obj = models.Student(user_name, password)
    student_obj.save()

    return True, '学生[{}]注册成功'.format(user_name)

def student_choice_school_interface(school_name, stu_name):
    # 检测学生是否选择了学校
    student_obj = models.Student.select(stu_name)

    if student_obj.school:
        return False, '学生已经选择了学校,不能再次选择'

    # 调用Student,保存选择学校信息
    student_obj.choice_school(school_name)
    return True, '学生[{}]选择学校[{}]成功'.format(stu_name, school_name)

def student_check_school(stu_name):
    student_obj = models.Student.select(stu_name)
    return student_obj.get_school()

def student_choice_course_interface(course_name, stu_name):
    student_obj = models.Student.select(stu_name)

    # 检测学生是否已经选择了该课程
    if course_name in student_obj.course_list:
        return False, '学生已经选择过该课程'

    student_obj.choice_course(course_name)
    return True, '学生[{}]选择课程[{}]成功'.format(stu_name, course_name)

def student_get_score_interface(stu_name):
    student_obj = models.Student.select(stu_name)
    return student_obj.get_score()
