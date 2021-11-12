# todos/serializers.py
# https://wsvincent.com/django-rest-framework-react-tutorial/

from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'user_id',
        )
        model = Todo
