from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studyIndex', views.hello, name='hello')
]