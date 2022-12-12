from django.contrib import admin
from .models import (
    Expense, 
    Income, 
    CategoryExpense, 
    CategoryIncome
)

# Register your models here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]
    list_filter = [
        'id',
    ]
    


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]
    list_filter = [
        'id',
    ]

@admin.register(CategoryExpense)
class CategoryExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]
    list_filter = [
        'id',
    ]
    


@admin.register(CategoryIncome)
class CategoryIncomeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]
    list_filter = [
        'id',
    ]