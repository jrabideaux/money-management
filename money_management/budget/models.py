import uuid

from django.conf import settings
from django.db import models


# Create your models here.
class UserCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=32)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class UserPlanItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    JANUARY = 'JAN'
    FEBRUARY = 'FEB'
    MARCH = 'MAR'
    APRIL = 'APR'
    MAY = 'MAY'
    JUNE = 'JUN'
    JULY = 'JULY'
    AUGUST = 'AUG'
    SEPTEMBER = 'SEP'
    OCTOBER = 'OCT'
    NOVEMBER = 'NOV'
    DECEMBER = 'DEC'
    MONTH_CHOICES = [
        (JANUARY, 'January'),
        (FEBRUARY, 'February'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December')
    ]
    month_choice = models.CharField(
        max_length=100,
        choices=MONTH_CHOICES
    )
    YEAR_CHOICES = [
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
    ]
    year_choice = models.CharField(
        max_length=100,
        choices=YEAR_CHOICES,
        default='2021'
    )
    category = models.CharField(max_length=50)
    amount = models.IntegerField()
    expense = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
