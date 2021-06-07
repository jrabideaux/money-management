from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import UserPlanItem
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def get_expense_plan_items_current_month(request):
    if request.user.is_authenticated:
        current_date=datetime.today()
        current_month=current_date.strftime("%b").upper()
        current_year=current_date.year
        user=request.user
        plan_item_list = UserPlanItem.objects.filter(user_id=user).filter(month_choice=current_month, year_choice=current_year, expense=True)
    else:
        raise(PermissionError)
    return HttpResponse(plan_item_list)

def login_view(request):
    template = loader.get_template("login.html")
    username = request.POST('username')
    password = request.POST('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, '/login.html')