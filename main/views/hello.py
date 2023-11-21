from django.http import HttpResponse, Http404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import Hello
from main.serializers import HelloSerializer

from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


class HelloView(APIView):
    constHello = "this is Const Hello"

    def get_obj(self, pk):

        try:
            return Hello.objects.get(pk=pk)
        except Hello.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        pk is primary key是主键id的意思
        """
        hello = self.get_obj(pk)
        serializer = HelloSerializer(hello)
        return Response(serializer.data)

    def post(self, request):
        ...

    def put(self, request, pk):
        snippet = self.get_obj(pk)
        print(request.data)  # 这个是获取请求体
        serializer = HelloSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_obj(pk)
        snippet.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    ...
