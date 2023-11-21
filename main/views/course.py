from django.http import JsonResponse
from django.views import View

from main.models import Course


class CourseInitView(View):
    @staticmethod
    def get(req):
        """初始化学科，通过get请求触发操作"""
        Course.objects.create(name="语文", max_score=150)
        Course.objects.create(name="数学", max_score=150)
        Course.objects.create(name="英语", max_score=150)
        Course.objects.create(name="物理", max_score=110)
        Course.objects.create(name="化学", max_score=100)
        Course.objects.create(name="生物", max_score=90)
        Course.objects.create(name="政治", max_score=110)
        Course.objects.create(name="历史", max_score=100)
        Course.objects.create(name="地理", max_score=90)
        return JsonResponse({
            'text': 'success'
        })


class CourseView(View):
    @staticmethod
    def get(req):
        return JsonResponse({
            "data": list(Course.objects.values("name", "max_score"))
        })
