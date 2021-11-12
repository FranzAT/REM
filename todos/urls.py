# todos/urls.py
# https://wsvincent.com/django-rest-framework-react-tutorial/

from django.urls import path

from . import views


urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
]
