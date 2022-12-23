from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from money.models import CategoryExpense, CategoryIncome, Expense, Income

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", email="test")
        user.set_password("12345")
        user.save()
        self.clientE = Client()
        self.client.login(username="testuser", password="12345")
        self.categoryE = CategoryExpense.objects.create(
            name="Teste",
            creation_user=user
        )

        self.expense = Expense.objects.create(
            id=1,
            name="teste",
            value=20,
            category=self.categoryE,
            creation_user=user
            
            )
        self.categoryI = CategoryIncome.objects.create(
            name="Teste",
            creation_user=user
        )

        self.expense = Income.objects.create(
            id=1,
            name="teste",
            value=20,
            category=self.categoryI,
            creation_user=user
            
            )
    def test_expense_list(self):
        response = self.client.get(reverse("expenses"))
        self.assertEqual(response.status_code,200)

    def test_income_list(self):
        response = self.client.get(reverse("incomes"))
        self.assertEqual(response.status_code,200)
    
    def test_expense_form(self):
        response = self.client.post(reverse("expense_new"), data={
            'name':'testando',
            'value':20,
            'category':self.categoryE

        })
        self.assertEqual(response.status_code,200)
    
    def test_income_form(self):
        response = self.client.post(reverse("income_new"), data={
            'name':'testando',
            'value':20,
            'category':self.categoryI

        })
        self.assertEqual(response.status_code,200)
