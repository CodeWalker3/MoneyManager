
from django.contrib import admin
from django.urls import path, include
from .views import(
    MyExpenses, 
    CreateExpense, 
    MyIncomes, 
    CreateIncome, 
    ExpenseDelete, 
    IncomeDelete,
    ChartExpense,
    ChartIncome,

    CreateCategoryExpense,
    CreateCategoryIncome
    )
urlpatterns = [
    path('expenses', MyExpenses.as_view(), name='expenses'),
    path('new_expense', CreateExpense.as_view(), name='expense_new'),
    path('incomes', MyIncomes.as_view(), name='incomes'),
    path('new_income', CreateIncome.as_view(), name='income_new'),
    path('category_income_new', CreateCategoryIncome.as_view(), name='category_income_new'),
    path('category_expense_new', CreateCategoryExpense.as_view(), name='category_expense_new'),
    path('incomesd/<int:pk>', IncomeDelete.as_view(), name='incomes_del'),
    path('expensesd/<int:pk>', ExpenseDelete.as_view(), name='expense_del'),
    path('chart_expense', ChartExpense.as_view(), name='chart_expense'),
    path('chart_income', ChartIncome.as_view(), name='chart_income'),
]
