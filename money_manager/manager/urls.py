from django.urls import path
from .views import TransactionListView,CreateTransactionView

urlpatterns = [
    path('all/', TransactionListView.as_view()),
    path('create/', CreateTransactionView.as_view()),
]
