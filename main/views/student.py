"""

"""
from django.http import JsonResponse
from django.db import transaction
from main.models import School, ClassRoom, Student, UnionExam, Course, UnionExamCourseScore
from main.tools.randomName import get_random_name


@transaction.atomic
def add_student(request):
    """
    涌入一批学生
    遍历每一个学校的每一个班级，如果该班级不够40人，则随机生成学生补齐
    """
    try:
        # 遍历每一个学校
        schools = School.objects.all()

        for school in schools:
            print(school)
            class_rooms = ClassRoom.objects.filter(school_id=school)
            for class_room in class_rooms:
                # 看看这个班级有多少学生
                count = Student.objects.filter(class_room_id=class_room).count()
                print('\t', class_room, count)
                if count >= 40:
                    continue
                # 如果这个班不足40个学生，则随机生成学生补齐40个
                students = [
                    Student(
                        name=get_random_name(),
                        class_room_id=class_room
                    ) for _ in range(40 - count)
                ]
                Student.objects.bulk_create(students)

        return JsonResponse({
            'text': 'success'
        })
    except Exception as e:
        return JsonResponse({
            'text': f'fail, {e}'
        })


def query_student_score_history(req):
    """
    查询一个学生的分数历史
    """
    try:
        student_id = req.GET.get('id', 1)

        history = []
        titles = []
        for exam in UnionExam.objects.all():
            # 遍历所有的联考数据
            titles.append(exam.name)
            history_item = []
            for course in Course.objects.all():
                # 遍历所有的科目
                score = UnionExamCourseScore.objects.get(
                    student_id=student_id,
                    exam_id=exam,
                    course_id=course,
                )
                history_item.append({
                    "name": course.name,
                    "score": score.score,
                })
            history.append(history_item)

        sum_history = []
        for exam in history:
            sum_score = 0
            for course in exam:
                sum_score += course["score"]
            sum_history.append(sum_score)

        avg_history = [round(sum_score / 9, 2) for sum_score in sum_history]

        return JsonResponse({
            'status': True,
            'data': {
                "titles": titles,
                "history": history,
                "sum_history": sum_history,
                "avg_history": avg_history
            }
        })
    except UnionExamCourseScore.DoesNotExist:
        return JsonResponse({
            'status': False,
            'text': '学生不存在',
            'data': {}
        }, status=404)
