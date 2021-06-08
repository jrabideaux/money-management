from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic
from .models import UserPlanItem
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class UserCurrentMonthPlanView(generic.ListView):

    template_name = "plan.html"
    context_object_name = 'plan_item_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            current_date=datetime.today()
            current_month=current_date.strftime("%b").upper()
            current_year=current_date.year
            user=self.request.user
            return UserPlanItem.objects.filter(user_id=user.id).filter(month_choice=current_month, year_choice=current_year)
        else:
            raise(PermissionError)

def login_view(request):
    template = loader.get_template("login.html")
    username = request.POST('username')
    password = request.POST('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, '/login.html')