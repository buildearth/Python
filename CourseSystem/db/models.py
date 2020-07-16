'''
存放类
角色:学校,学生,课程,老师,管理员
'''
from db import db_handler

class Base:
    # 共同的方法属性放到基类中
    def save(self):
        # 调用数据处理层保存数据
        db_handler.save(self)

    @classmethod
    def select(cls, user_name):
        return db_handler.select(cls, user_name)

class Admin(Base):
    def __init__(self, user_name, password):
        self.user = user_name
        self.pwd = password

    def create_school(self, school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_course(self, course_name, school_obj):
        course_obj = Course(course_name)
        course_obj.save()

        school_obj.course_list.append(course_name)
        school_obj.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()

class School(Base):
    def __init__(self, school_name, school_addr):
        self.user = school_name
        self.addr = school_addr
        self.course_list = []

    def get_course(self):
        return self.course_list

class Student(Base):
    def __init__(self, user_name, password):
        self.user = user_name
        self.pwd = password
        self.school = None
        self.course_list = []
        self.score_dict = {}

    def choice_school(self, school_name):
        self.school = school_name
        self.save()

    def get_school(self):
        return self.school

    def choice_course(self, course_name):
        self.course_list.append(course_name)
        self.score_dict[course_name] = 0
        self.save()
        # 关联到课程
        course_obj = Course.select(course_name)
        course_obj.add_student(self.user)

    def get_score(self):
        return self.score_dict


class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []

    def get_student(self):
        return self.student_list

    def add_student(self, student_name):
        self.student_list.append(student_name)
        self.save()

class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list_from_teacher = []

    def get_course(self):
        return self.course_list_from_teacher

    def choice_course(self, course_name):
        self.course_list_from_teacher.append(course_name)
        self.save()

    def change_score(self, student_name, course_name, score):
        student_obj = Student.select(student_name)
        student_obj.score_dict[course_name] = score
        student_obj.save()

