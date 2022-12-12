from django import forms

from .models import Expense, Income, CategoryIncome, CategoryExpense

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = [
            'name',
            'value',
            'typeexpense',
            'category',
        ]
    category = forms.ModelChoiceField(queryset=CategoryExpense.objects.all())
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')

        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = self.fields['category'].queryset.filter(
            creation_user=request.user)


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            'name',
            'value',
            'typeincome',
            'category',
        ]
    category = forms.ModelChoiceField(queryset=CategoryIncome.objects.all())
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')

        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = self.fields['category'].queryset.filter(
            creation_user=request.user)

class CategoryExpenseForm(forms.ModelForm):
    
    class Meta:
        model = CategoryExpense
        fields = ['name']

class CategoryIncomeForm(forms.ModelForm):
    
    class Meta:
        model = CategoryIncome
        fields = ['name']

field_category_income = IncomeForm.base_fields['category']
field_category_expense = ExpenseForm.base_fields['category']
field_category_income.widget.attrs["class"] = "form__field"
field_category_expense.widget.attrs["class"] = "form__field"

