"""money_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from budget import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', views.UserCurrentMonthPlanView.as_view(),
         name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('categories/list', views.UserCategoriesListView.as_view(),
         name='list'),
    path('categories/add', views.add_category,
         name='add'),
    path('categories/delete/<pk>',
         views.UserCategoriesDeleteView.as_view(), name="delete"),
    path('categories/edit/<pk>', views.UserCategoriesUpdateView.as_view(),
         name="edit")

]
