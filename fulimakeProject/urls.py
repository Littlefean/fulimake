from django.contrib import admin

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from main.views.viewset import UserViewSet, GroupViewSet


# 序列化器是用来定义API的表示形式。
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# 路由器提供一个简单自动的方法来决定URL的配置。
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('main/', include("main.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
