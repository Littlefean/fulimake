from django.db import transaction
from django.http import JsonResponse
from django.views import View

from main.models import Government, School, ClassRoom, Teacher, Student
from random import randint, choice, sample

from ..tools.randomName import get_random_name


class SchoolView(View):
    @staticmethod
    def get(_):
        """
        获取一个学校里所有的班级、以及每个班级对应的学生
        """
        res = []
        for school in School.objects.all():
            school_obj = {
                "name": school.name,
                "classes": []
            }
            for class_room in ClassRoom.objects.filter(school_id=school):
                students = Student.objects.filter(class_room_id=class_room).values('name')
                school_obj["classes"].append({
                    "className": str(class_room),
                    "students": list(students)
                })
                print(students)
            res.append(school_obj)
        return JsonResponse({
            "data": res
        })

    @transaction.atomic
    def post(self, request):
        """随机增加一个学校"""
        try:

            # 随机绑定一个政府
            gov = choice(Government.objects.all())

            school = School.objects.create(
                name=f'世界第{randint(1, 1000000)}中学',
                government_id=gov,
            )

            # 批量创建10*老师
            teachers = [Teacher(name=get_random_name(), school_id=school) for _ in range(10)]
            Teacher.objects.bulk_create(teachers)

            # 批量创建班级
            classrooms = [ClassRoom(grade=2019, class_number=i, school_id=school) for i in range(1, 10)]
            ClassRoom.objects.bulk_create(classrooms)

            # 将每个班级绑定四个老师
            for cls in classrooms:
                # 从已经创建的老师列表（teachers）中随机选择 4 个老师
                selected_teachers = sample(teachers, 4)
                print(selected_teachers)
                # 将选定的老师与当前班级绑定起来
                cls.teachers.add(*selected_teachers)

            return JsonResponse({
                'text': "success"
            })
        except Exception as e:
            return JsonResponse({
                'text': f'{e}'
            })
