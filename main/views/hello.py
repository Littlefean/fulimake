from django.http import HttpResponse
from django.views import View


class HelloView(View):
    constHello = "this is Const Hello"

    def get(self, request, *args, **kwargs):
        return HttpResponse(f"hello1 {str(request)} {self.constHello}")

    ...
