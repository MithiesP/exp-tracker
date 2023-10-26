# expense_tracker/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('update/<int:expense_id>/', views.update_expense, name='update_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
