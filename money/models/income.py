from django.db import models
from .category_income import CategoryIncome
# Create your models here.
class Income(models.Model):

    CHOICE_INCOME = (
        ('Monthly','Monthly'),
        ('Period','Period'),
        ('Extra','Extra'),
    )
    name = models.CharField(
        verbose_name="Name of the income",
        max_length=40,
        null=False, blank=False
    )
    value = models.DecimalField(
        verbose_name="Value of the income",
        decimal_places=2,
        max_digits=32,
        max_length=40,
        null=False, blank=False
    )
    typeincome = models.CharField(
        verbose_name="Type of the income",
        max_length= 30,
        choices = CHOICE_INCOME,
    )
    category = models.ForeignKey(
        CategoryIncome,
        verbose_name="Category of the income",
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
    def __str__(self):
        return self.name