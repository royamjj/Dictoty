from django.shortcuts import redirect, render
from .models import Todo


def index(request):

     if request.method == 'POST':
          new_todo = Todo(title = request.POST['title'])
          if len(new_todo.title) == 0:
               return redirect('/todoList')
          new_todo.save()
          return redirect('/todoList')
     todos = Todo.objects.all()
     return render(request, 'todoList/index.html', {'todos':todos})


def delete(request, pk):
     todo = Todo.objects.get(id=pk)
     todo.delete()
     return redirect('/todoList')