import json
import random

from django.http import JsonResponse, HttpResponse
from django.views import View

from main.models import Government


def test(request):
    try:
        data = {
            "user": "jack",
            "pwd": "123",
        }
        if request.method == "OPTIONS":
            print("options test")
            return HttpResponse(headers={"Access-Control-Allow-Origin": "*"})
        if request.method == 'GET':
            return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        return JsonResponse({
            'text': f'{e}'
        })


class TestView(View):
    @staticmethod
    def get(request):
        rand_name = f"ABAB{random.randint(0, 100000)}"
        government = Government.objects.create(name=rand_name)
        print(government)

        return HttpResponse(json.dumps({
            "text": 'success',
            "data": rand_name
        }), status=200, content_type='application/json')
