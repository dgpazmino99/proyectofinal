from django.shortcuts import render
from .models import Task
from .models import Board
# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def board_view(request, board_id):
    board = Board.objects.get(id=board_id)
    columns = board.column_set.all()
    tasks = Task.objects.filter(column__in=columns)
    return render(request, 'board.html', {'board': board, 'columns': columns, 'tasks': tasks})

def index(request):
    return render(request, 'myapp/index.html')

