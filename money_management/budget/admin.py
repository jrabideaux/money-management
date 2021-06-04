from django.contrib import admin
from .models import UserCategory
from .models import UserPlanItem

# Register your models here.

admin.site.register(UserCategory)
admin.site.register(UserPlanItem)