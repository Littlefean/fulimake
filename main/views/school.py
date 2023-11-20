from django.db import transaction
from django.http import JsonResponse

from main.models import Government, School, ClassRoom, Teacher, Student
from random import randint, choice, sample

from ..tools.randomName import get_random_name


@transaction.atomic
def add_random_school(request):
    """
    生成一个学校，并随机绑定一个现有的政府
    并随机生成一些老师和班级
    """
    try:
        if request.method != "GET":
            raise Exception("请求方法错了")

        # 随机绑定一个政府
        gov = choice(Government.objects.all())

        school = School.objects.create(
            name=f'世界第{randint(1, 1000000)}中学',
            government_id=gov,
        )

        # 批量创建10*老师
        teachers = [Teacher(name=get_random_name(), school_id=school) for _ in range(10)]
        Teacher.objects.bulk_create(teachers)

        # 开始随机生成班级，一下子创建是个班级
        # for i in range(1, 10):
        #     cls = ClassRoom.objects.create(
        #         grade=2019,
        #         class_number=i,
        #         school_id=school
        #     )
        #     # 给这个班级随机分配四个老师
        #     # 踩坑：cls不能直接.add，要在它的多对多key上调用add方法
        #     cls.teachers.add(*sample(teachers, 4))

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


def show_all_school(request):
    assert request.method == "GET"
    # [{name: schoolName, classes: [{className: str, student: [{name: str}]}]}]
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