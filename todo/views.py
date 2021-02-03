from django.shortcuts import render, redirect
from .models import Column, Todo
from .forms import ColumnForm, TodoForm

''''
    This is the base view, it retrives the list of columns and todos ...
    from database and send it to the index.html page
'''
def index(request):
    column_list = Column.objects.all()
    todo_list = Todo.objects.all()
    context_dic = {"columns": column_list, "todos": todo_list}
    return render(request, 'todo/index.html', context_dic)


'''
    This view gets invoked from the home page (index.html)
    Obtains the data sent from the form and save it to the database
    Else it returns the form to be filled
'''
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


'''
    This view gets invoked from the home page
    It is used to add new todo to the database
    If the request is post and the form is sent, this view saves it to the database
    Else it returns the form to be filled
'''
def addTodo(request, column=None):
    todo_form = TodoForm()
    column_list = Column.objects.all()
    context_dic = {'todo_form': todo_form, "column": column}

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
            print(todo_form.errors)
    else:
        context_dic["columns"] = column_list
    return render(request, 'todo/add_todo.html', context_dic)

# def link_redirect(request, link=None):
#     print("************")
#     print(link)
#     return redirect(link)