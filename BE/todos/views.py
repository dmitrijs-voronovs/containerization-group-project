from django.shortcuts import get_object_or_404
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Todo

@csrf_exempt
def todo_list(request):
    todos = Todo.objects.all()
    data = {"results": list(todos.values("id", "title", "completed"))}
    return JsonResponse(data)

@csrf_exempt
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
    return JsonResponse(data)

@csrf_exempt
def todo_create(request):
    if request.method == "POST":
        body = json.loads(request.body)
        todo = Todo.objects.create(title=body.get("title", "Empty TODO 2"))
        data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
        return JsonResponse(data)

@csrf_exempt
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "PUT":
        body = json.loads(request.body)
        todo.title = body.get("title", todo.title)
        todo.completed = body.get("completed", todo.completed)
        todo.save()
        data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
        return JsonResponse(data)

@csrf_exempt
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "DELETE":
        todo.delete()
        return JsonResponse({"message": "Todo was deleted."})