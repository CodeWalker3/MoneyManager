from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import Expense, Income, CategoryExpense, CategoryIncome
from django.views.generic.edit import CreateView
from .forms import ExpenseForm, IncomeForm, CategoryExpenseForm, CategoryIncomeForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.paginator import Paginator

colorPalette = ['#55efc4', '#81ecec', '#a29bfe', '#ffeaa7', '#fab1a0', '#ff7675', '#fd79a8']
colorPrimary, colorSuccess, colorDanger = '#79aec8', colorPalette[0], colorPalette[5]
# Create your views here.
@login_required(login_url='login')
def my_expenses(request):

    expenses = Expense.objects.filter(creation_user=request.user).filter(category__creation_user=request.user).order_by('name')
    total_expense = 0
    incomes = Income.objects.filter(creation_user=request.user).filter(category__creation_user=request.user).order_by('name')
    total_income = 0
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for expense in expenses:
        total_expense += expense.value
    for income in incomes:
        total_income += income.value
    
    return render(
        request, 'my_expenses.html',{
            'expenses': page_obj,
            'total_expense':total_expense,
            'total_income':total_income,
            'remaining':(total_income-total_expense)

        }
    )
@method_decorator(login_required, name='dispatch')
class CreateExpense(CreateView):
    model = Expense
    form_class   = ExpenseForm
    template_name="expense_form.html"

    def get_form_kwargs(self):
        kwargs = super(CreateExpense, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse_lazy('expenses')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creation_user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())

@login_required(login_url='login')
def my_incomes(request):
    expenses = Expense.objects.filter(creation_user=request.user).filter(category__creation_user=request.user).order_by('name')
    total_expense = 0
    incomes = Income.objects.filter(creation_user=request.user).filter(category__creation_user=request.user).order_by('name')
    total_income = 0

    for expense in expenses:
        total_expense += expense.value
    for income in incomes:
        total_income += income.value

    paginator = Paginator(incomes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'my_incomes.html',{
            'incomes': page_obj,
            'total_expense':total_expense,
            'total_income':total_income,
            'remaining':(total_income-total_expense)
        }
    )
@method_decorator(login_required, name='dispatch')
class CreateIncome(CreateView):
    model = Income
    form_class   = IncomeForm
    template_name="income_form.html"

    def get_form_kwargs(self):
        kwargs = super(CreateIncome, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse_lazy('incomes')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creation_user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class CreateCategoryExpense(CreateView):
    model = CategoryExpense
    form_class= CategoryExpenseForm
    template_name="category_expense_form.html"

    def get_success_url(self):
        return reverse_lazy('expenses')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creation_user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class CreateCategoryIncome(CreateView):
    model = CategoryIncome
    form_class= CategoryIncomeForm
    template_name="category_income_form.html"

    def get_success_url(self):
        return reverse_lazy('incomes')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creation_user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())

@login_required
def income_delete(request,id):
    income = Income.objects.filter(id=id).first()
    income.delete()
    return redirect('incomes')
@login_required
def expense_delete(request,id):
    expense = Expense.objects.filter(id=id).first()
    expense.delete()
    return redirect('expenses')

def chart_expense(request):
    labels = []
    data = []
    context={
        'labels': labels,
        'data': data,
    }
    queryset = Expense.objects.values('category__name').annotate(category_value=Sum('value')).order_by('-category_value').filter( creation_user = request.user).filter(category__creation_user=request.user)
    for expense in queryset:
        labels.append(expense['category__name'])
        data.append(expense['category_value'])

    return JsonResponse(context)

def chart_income(request):
    labels = []
    datas = []
    context={
        'labels': labels,
        'data': datas,
    }
    queryset = Income.objects.values('category__name').annotate(category_value=Sum('value')).order_by('-category_value').filter( creation_user = request.user).filter(category__creation_user=request.user)
    for income in queryset:
        labels.append(income['category__name'])
        datas.append(income['category_value'])

    return JsonResponse(context)




