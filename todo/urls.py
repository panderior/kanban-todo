from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add_column/', addColumn, name='add_column'),
    path('add_todo/', addTodo, name='add_todo'),
]