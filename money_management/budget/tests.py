from django.contrib.auth.models import User
from django.test import TestCase

from .models import UserCategory, UserPlanItem


# Create your tests here.
class CategoryModelTests(TestCase):

    def test_category_created(self):
        user = User.objects.create(first_name="Josh")
        obj = UserCategory(category="Home", user=user)
        obj.save()
        saved_object = UserCategory.objects.all()
        self.assertEquals(saved_object[0].category, 'Home')


class UserPlanItemTests(TestCase):

    def test_create_item(self):
        user = User.objects.create(first_name="Josh")
        user.save()
        test_plan_item = UserPlanItem.objects.create(month_choice="JAN",
                                                     year_choice="2022",
                                                     category="Gaming",
                                                     amount=60,
                                                     expense=False, user=user)
        test_plan_item.save()
        obj = UserPlanItem.objects.all()
        self.assertEquals(obj[0].month_choice, 'JAN')
        self.assertEquals(obj[0].year_choice, '2022')
        self.assertEquals(obj[0].category, 'Gaming')
        self.assertEquals(obj[0].amount, 60)
        self.assertEquals(obj[0].expense, False)
