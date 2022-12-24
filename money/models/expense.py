from django.db import models
from .category_expense import CategoryExpense
# Create your models here.
class Expense(models.Model):

    CHOICE_EXPENSE = (
        ('Monthly','Monthly'),
        ('Period','Period'),
        ('Extra','Extra'),
        ('Day by day','Day by day')
    )
    name = models.CharField(
        verbose_name="Name of the expense",
        max_length=40,
        null=False, blank=False
    )
    value = models.DecimalField(
        verbose_name="Value of the expense",
        decimal_places=2,
        max_digits=32,
        max_length=40,
        null=False, blank=False
    )
    typeexpense = models.CharField(
        verbose_name="Type of the expense",
        max_length= 30,
        choices = CHOICE_EXPENSE,
    )
    category = models.ForeignKey(
        CategoryExpense,
        verbose_name="Category of the expense",
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    creation_date = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True
    )
    creation_user = models.ForeignKey(
        'auth.User', 
        related_name='%(class)s_requests_created',
        blank=True, null=True,
        default=None,
        on_delete=models.SET_NULL
    )
	
    updated_user = models.ForeignKey(
        'auth.User', 
        related_name='%(class)s_requests_modified',
        blank=True, null=True,
        default=None,
        on_delete=models.SET_NULL
    )
