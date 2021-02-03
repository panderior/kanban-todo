from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add_column/', addColumn, name='add_column'),
    path('add_todo/<str:column>/', addTodo, name='add_todo'),
    path('add_todo/', addTodo, name='add_todo'),
    # path('redirect/<str:link>/', link_redirect, name='link_redirect'),
]