from datetime import datetime

from django.http import JsonResponse
from django.utils.timezone import make_aware

from main.models import UnionExam, School, Course, UnionExamCourseScore, ClassRoom, Student
import random

from main.tools.randomScore import get_random_score


def create_and_test(req):
    """
    随机生成一个联考并让全部学校统一参加一次考试
    全国性质的联考
    这个功能目前非常耗时，需要3-5秒
    """
    exam_count = UnionExam.objects.count()
    start_date = make_aware(datetime.now())
    # 创建联考
    exam = UnionExam.objects.create(
        name=f'全国第{exam_count + 1}次联考',
        start_date=start_date
    )
    # 遍历每一个学生，他们都开始考试
    # 每个学生都有一定的概率缺考、作弊被抓
    for student in Student.objects.filter():
        is_cheated = False
        for course in Course.objects.all():
            # 是否睡过头了忘了参加考试
            absent = random.random() < 0.001  # 0.1% 的概率睡过头
            # 是否在这科目的考试中企图作弊？
            cheat = random.random() < 0.005  # 0.5% 的概率作弊并且被发现了

            if absent or cheat:
                score = 0
            else:
                score = get_random_score(course.max_score)

            # 如果本次考试的之前的科目已经出现过作弊了，那么剩下的考试都不用来了，缺考
            if is_cheated:
                score = 0
                absent = True
            UnionExamCourseScore.objects.create(
                student_id=student,
                exam_id=exam,
                course_id=course,
                score=score,
                absent=absent,
                cheat=cheat
            )
            if cheat:
                is_cheated = True
    return JsonResponse({
        "status": True
    })
