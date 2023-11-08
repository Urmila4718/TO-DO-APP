from django.urls import path

from todo.views import index,remove


urlpatterns = [
    path('', index,name="todo"),
    path('del/<str:item_id>', remove, name="del"),
]
