from datetime import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.template import loader
from django.views import generic
from django.forms import forms

from .models import UserPlanItem, UserCategory
from .forms import CategoryForm

# Create your views here.

class UserCurrentMonthPlanView(generic.ListView):
    template_name = "plan.html"
    context_object_name = 'plan_item_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            current_date = datetime.today()
            current_month = current_date.strftime("%b").upper()
            current_year = current_date.year
            user = self.request.user
            return UserPlanItem.objects.filter(user_id=user.id).filter(
                month_choice=current_month, year_choice=current_year)
        else:
            raise PermissionError


class UserCategoriesListView(generic.ListView):
    template_name = "categories/list.html"
    context_object_name = 'category_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UserCategory.objects.filter(user_id=self.request.user.id)


def login_view(request):
    loader.get_template("login.html")
    username = request.POST('username')
    password = request.POST('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, '/login.html')


def add_category(request):
    form = CategoryForm(request.POST)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CategoryForm(request.POST)
    return render(request, 'categories/add.html', {'form' : form})


