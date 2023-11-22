from django.http import HttpResponse, Http404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import Hello
from main.serializers import HelloSerializer

from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework import generics


class HelloList(generics.ListCreateAPIView):
    """
    GET请求：可以使用请求URL 'http://example.com/hello-list/' 获取所有 Hello 对象的列表。
    POST请求：可以使用请求URL 'http://example.com/hello-list/' 在服务器上创建新的 Hello 对象。
    """
    # 两行代码写出一个接口，离谱

    queryset = Hello.objects.all()
    serializer_class = HelloSerializer
    ...


class HelloDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET请求：可以使用请求URL 'http://example.com/hello-detail/<id>/' 获取具有特定 id 的 Hello 对象的详细信息。
    PUT请求：可以使用请求URL 'http://example.com/hello-detail/<id>/' 更新具有特定 id 的 Hello 对象的信息。
    PATCH请求：可以使用请求URL 'http://example.com/hello-detail/<id>/' 部分更新具有特定 id 的 Hello 对象的信息。
    DELETE请求：可以使用请求URL 'http://example.com/hello-detail/<id>/' 删除具有特定 id 的 Hello 对象。
    """
    # 两行代码写出一个接口，离谱
    queryset = Hello.objects.all()
    serializer_class = HelloSerializer


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
