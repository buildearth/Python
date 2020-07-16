from db import models

def teacher_check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    return teacher_obj.get_course()

def teacher_choice_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if course_name in teacher_obj.course_list_from_teacher:
        return False, '该课程老师已经选择过了'

    teacher_obj.choice_course(course_name)
    return True, '老师[{}] 选择教授课程[{}]成功'.format(teacher_name, course_name)

def teacher_change_score_interface(student_name, course_name, score, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    teacher_obj.change_score(student_name, course_name, score)
