from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    data = {"results": list(todos.values("id", "title", "completed"))}
    return JsonResponse(data)

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
    return JsonResponse(data)

def todo_create(request):
    if request.method == "POST":
        todo = Todo.objects.create(title=request.POST["title"])
        data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
        return JsonResponse(data)

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "PUT":
        todo.title = request.PUT.get("title", todo.title)
        todo.completed = request.PUT.get("completed", todo.completed)
        todo.save()
        data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
        return JsonResponse(data)

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "DELETE":
        todo.delete()
        return JsonResponse({"message": "Todo was deleted."})