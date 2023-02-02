from django.shortcuts import get_object_or_404
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

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
        todo = Todo.objects.create(title=request.POST.get("title", "Empty TODO"))
        data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
        return JsonResponse(data)

@csrf_exempt
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "PUT":
        todo.title = QueryDict(request.body).get("title", todo.title)
        todo.completed = QueryDict(request.body).get("completed", todo.completed)
        todo.save()
        data = {"id": todo.id, "title": todo.title, "completed": todo.completed}
        return JsonResponse(data)

@csrf_exempt
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "DELETE":
        todo.delete()
        return JsonResponse({"message": "Todo was deleted."})