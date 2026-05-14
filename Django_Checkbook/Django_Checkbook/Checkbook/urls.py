from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),  # url path for the app's home page
    path('create/', views.create_account, name='create'),  # url path for creating an account
    path('<int:pk>/balance/', views.balance, name='balance'),  # url for a specific account's balance. pk is passed
    path('transaction/', views.transaction, name='transaction'),  # url to add a transaction
]