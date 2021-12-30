import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def monday(request):
    todo_list = ['Wash the dishes', 'Do homework', 'go outside']
    random.shuffle(todo_list)
    return render(request, 'monday.html', {'todo_list': todo_list})

def tuesday(request):
    todo_list = ['Go outside', 'Work out', 'play videogames']
    random.shuffle(todo_list)
    return render(request, 'tuesday.html', {'todo_list': todo_list})

def wednesday(request):
    todo_list = ['eat breakfast', 'work out', 'do homework']
    random.shuffle(todo_list)
    return render(request, 'wednesday.html', {'todo_list': todo_list})