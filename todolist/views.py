from django.shortcuts import render, redirect
from .models import TodoList
from category.models import Category
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def my_todos(request):
    user = request.user
    now = timezone.now().strftime("%Y-%m-%d")
    
    # Fetch all tasks for the user
    todos = TodoList.objects.filter(user=user)
    
    # Fetch categories
    category1 = Category.objects.get(id=1) 
    category2 = Category.objects.get(id=2) 
    category3 = Category.objects.get(id=3) 
    
    # Get task counts based on categories
    Task_ID_Business = TodoList.objects.filter(category__name="Business", user=user) 
    Task_ID_Personal = TodoList.objects.filter(category__name="Personal", user=user)
    Task_ID_Other = TodoList.objects.filter(category__name="Other", user=user)

    no_of_Task_ID_Business = len(Task_ID_Business)
    no_of_Task_ID_Personal = len(Task_ID_Personal)
    no_of_Task_ID_Other = len(Task_ID_Other)
    
    # Pass additional context variables for priority and progress
    context = {
        "DateNow": now,
        "todos": todos, 
        "username": user.username,
        "category_i": category1.name,
        "category_ii": category2.name,
        "category_iii": category3.name,
        "no_of_business_tasks": no_of_Task_ID_Business,
        "no_of_other_tasks": no_of_Task_ID_Other,
        "no_of_personal_tasks": no_of_Task_ID_Personal,
    }

    return render(request, "todolist/home.html", context)
