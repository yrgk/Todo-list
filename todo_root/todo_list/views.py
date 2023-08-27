from django.shortcuts import redirect, render
from .models import *
from .forms import *



def index(request):
    all_tasks = TodoList.objects.all()[::-1]
    length = len(all_tasks)
    return render(request, 'todo_list/index.html', {'all_tasks':all_tasks, 'length':length,'title':'Main Page'})


def add_to_list(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'todo_list/addtask.html', {'form': form, 'title':'Add Task'})


def complete(request, post_slug):
    TodoList.objects.filter(slug=post_slug).delete()
    return redirect('home')


def edit(request, post_slug):

    post = TodoList.objects.filter(slug=post_slug)[0]

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            post.name = request.POST.get('name')
            post.content = request.POST.get('content')
            post.slug = request.POST.get('slug')
            post.save()
            return redirect('home')
    else:
        form = TodoForm(initial={'name':post.name, 'content':post.content, 'slug':post.slug})

    return render(request, 'todo_list/edit.html', {'post': post, 'form':form, 'title':'Edit'})