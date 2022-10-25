from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem


# Create your views here.
# Here we’re returning the list ‘all_todo_items’ as ‘all_items’ via a dictionary.

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def addTodoView(request):
    add = request.POST['content']
    new_item = TodoListItem(content=add)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    rem = TodoListItem.objects.get(id=i)
    rem.delete()
    return HttpResponseRedirect('/todoapp/')
