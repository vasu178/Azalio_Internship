from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.index, name='index'),
    path('class/', views.MyView.as_view(), name='my-view'),
]