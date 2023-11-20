from django.db import models


class Government(models.Model):
    """政府"""
    objects = models.Manager()
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class School(models.Model):
    """学校"""
    objects = models.Manager()

    name = models.CharField(max_length=30, unique=True)
    government_id = models.ForeignKey(Government, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=10)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    objects = models.Manager()
    grade = models.IntegerField()
    class_number = models.IntegerField()
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"{self.grade}级 {self.class_number}班"


# 多对多的中间表不用手动创建制定，他能自动创建

class Course(models.Model):
    objects = models.Manager()
    # 科目的名字，例如“历史”，由于考虑到一些特殊的科目可能名字会长的离谱，整了20个字
    name = models.CharField(max_length=20, unique=True)
    max_score = models.IntegerField()  # 这个科目的最高分
    ...


class Student(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=10)
    class_room_id = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    # 选择的课程，3+1+2， 只考虑1和2的部分 暂时先不做
    # select_courses = models.ManyToManyField(Course)
    ...


class UnionExam(models.Model):
    """单纯的联考"""
    objects = models.Manager()
    name = models.CharField(max_length=50)
    start_date = models.DateField()


class UnionExamCourseScore(models.Model):
    """所有学生、所有联考、每一科目的成绩"""
    objects = models.Manager()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(UnionExam, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    absent = models.BooleanField(default=False)
    cheat = models.BooleanField(default=False)


# ======== 下面是系统账号相关的内容：

class User(models.Model):
    objects = models.Manager()
    user_name = models.CharField(max_length=10)
    password_hash = models.CharField(max_length=50)
    ROLE_CHOICES = [
        (1, '政府'),
        (2, '学校'),
        (3, '老师'),
    ]
    role_number = models.IntegerField(choices=ROLE_CHOICES)
