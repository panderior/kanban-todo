from django.shortcuts import render, redirect
from .models import Column, Todo
from .forms import ColumnForm, TodoForm


def index(request):
    column_list = Column.objects.all()
    todo_list = Todo.objects.all()
    context_dic = {"columns": column_list, "todos": todo_list}
    return render(request, 'todo/index.html', context_dic)


def addColumn(request):
    column_form = ColumnForm()
    print(request.POST)
    if request.method == 'POST':
        column_form = ColumnForm(request.POST)
        if column_form.is_valid():
            column_form.save(commit=True)
            return redirect('/')
        else:
            print("Add Column Unsucessfull")
            print(column_form.errors)
    return render(request, 'todo/add_column.html', {'column_form': column_form})


def addTodo(request):
    todo_form = TodoForm()

    if request.method == 'POST':
        column = Column.objects.get(title=request.POST['column'])
        todo_post = {'title':request.POST['title'], 'description':request.POST['description'],
                                'column': column, 'palette':request.POST['palette'], 'link':request.POST['link']}
        todo_form = TodoForm(todo_post, request.FILES)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.column = column
            todo.save(0)
            return redirect('/')
        else:
            print("Add Column Unsucessfull")
            print(todo_form.errors)
    return render(request, 'todo/add_todo.html', {'todo_form': todo_form})