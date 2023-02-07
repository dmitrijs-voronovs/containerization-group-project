"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from todos import views;

urlpatterns = [
    path("todos/", views.todo_list, name="todo_list"),
    path("todos/<int:pk>/", views.todo_detail, name="todo_detail"),
    path("todos/create/", views.todo_create, name="todo_create"),
    path("todos/<int:pk>/update/", views.todo_update, name="todo_update"),
    path("todos/<int:pk>/delete/", views.todo_delete, name="todo_delete"),
]

# GKE:
# urlpatterns = [
#     path("api/todos/", views.todo_list, name="todo_list"),
#     path("api/todos/<int:pk>/", views.todo_detail, name="todo_detail"),
#     path("api/todos/create/", views.todo_create, name="todo_create"),
#     path("api/todos/<int:pk>/update/", views.todo_update, name="todo_update"),
#     path("api/todos/<int:pk>/delete/", views.todo_delete, name="todo_delete"),
# ]
