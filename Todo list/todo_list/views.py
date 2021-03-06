from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItems
# Create your views here.


def todoList(request):
    all_items = TodoItems.objects.all()
    return render(request, 'todo.html', {'list': all_items})


def addTodo(request):
    item = request.POST['content']
    add_item = TodoItems(content=item)
    add_item.save()
    return HttpResponseRedirect('/')


def deleteTodo(request, item_id):
    item = TodoItems.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/')
