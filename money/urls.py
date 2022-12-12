
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
    pie_chart
    )
urlpatterns = [
    path('expenses', my_expenses, name='expenses'),
    path('new_expense', CreateExpense.as_view(), name='expense_new'),
    path('incomes', my_incomes, name='incomes'),
    path('new_income', CreateIncome.as_view(), name='income_new'),
    path('incomesd/<int:id>', income_delete, name='incomes_del'),
    path('expensesd/<int:id>', expense_delete, name='expense_del'),
    path('chart_expense', chart_expense, name='chart_expense'),
    path('chart_income', chart_income, name='chart_income'),
    path('pie', pie_chart, name='pie_chart' )
]
