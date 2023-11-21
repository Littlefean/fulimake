from django.contrib.auth.models import User, Group
from rest_framework import serializers

from main.models import Hello


class HelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hello
        fields = 'name',


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
