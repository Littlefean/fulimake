from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from main.models import Government


@method_decorator(csrf_protect, name='dispatch')
class GovernmentView(View):

    @staticmethod
    def get(request):
        print("获取政府")
        try:
            government_list = list(Government.objects.all().values())
            return JsonResponse({
                "status": True,
                "text": 'success',
                "data": government_list
            }, status=200)
        except Exception as e:
            return JsonResponse({
                "text": f'{e}',
            }, status=500)

    @staticmethod
    def post(request):
        print("增加新的政府")

        try:
            name = request.POST.get('name')

            if not name:
                return JsonResponse({'text': '请输入政府名称'}, status=400)

            government = Government.objects.create(name=name)

            return JsonResponse({'id': government.id, 'name': government.name}, status=201)

        except Exception as e:
            return JsonResponse({
                "text": f'{e}',
            }, status=500)

    ...
