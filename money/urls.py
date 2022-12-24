
from django.contrib import admin
from django.urls import path, include
from .views import(
    my_expenses, 
    CreateExpense, 
    my_incomes, 
    CreateIncome, 
    expense_delete, 
    income_delete,
    chart_expense,
    chart_income,
    chart_income,
    CreateCategoryExpense,
    CreateCategoryIncome
    )
urlpatterns = [
    path('expenses', my_expenses, name='expenses'),
    path('new_expense', CreateExpense.as_view(), name='expense_new'),
    path('incomes', my_incomes, name='incomes'),
    path('new_income', CreateIncome.as_view(), name='income_new'),
    path('category_income_new', CreateCategoryIncome.as_view(), name='category_income_new'),
    path('category_expense_new', CreateCategoryExpense.as_view(), name='category_expense_new'),
    path('incomesd/<int:id>', income_delete, name='incomes_del'),
    path('expensesd/<int:id>', expense_delete, name='expense_del'),
    path('chart_expense', chart_expense, name='chart_expense'),
    path('chart_income', chart_income, name='chart_income'),
    path('pie', chart_income, name='pie_chart' )
]
